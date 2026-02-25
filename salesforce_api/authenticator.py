import os
import base64
import hashlib
import urllib.parse
import webbrowser
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
from PySide6.QtCore import QThread, Signal

# OAuth 2.0 (Authorization Code Flow + PKCE)
# redirect_uri: localhost:8080
# client_id = Consumer Key
class Authenticator(QThread):
    
    login_successful = Signal(dict)
    login_failed = Signal(str)

    def __init__(self, client_id, port=8080, login_url='https://login.salesforce.com'):
        super().__init__()
        self.client_id = client_id
        self.port = port
        self.login_url = login_url
        self.redirect_uri = f'http://localhost:{self.port}/callback'
        self.auth_code = None
        
        self._is_cancelled = False

    def cancel(self):
        self._is_cancelled = True

    def _generate_pkce(self): # -> code verifier, code challenge
        verifier_bytes = os.urandom(32)
        verifier = base64.urlsafe_b64encode(verifier_bytes).rstrip(b'=').decode('utf-8')
        
        # SHA256, Base64
        challenge_bytes = hashlib.sha256(verifier.encode('utf-8')).digest()
        challenge = base64.urlsafe_b64encode(challenge_bytes).rstrip(b'=').decode('utf-8')
        
        return verifier, challenge


    def run(self) -> dict:
        # returns a signal with: 'access_token', 'refresh_token', 'instance_url'
        try:
            verifier, challenge = self._generate_pkce()

            auth_url = (f'{self.login_url}/services/oauth2/authorize'
                        f'?client_id={self.client_id}'
                        f'&redirect_uri={urllib.parse.quote(self.redirect_uri)}'
                        f'&response_type=code'
                        f'&code_challenge={challenge}'
                        f'&code_challenge_method=S256')

            # handler for local server
            outer_self = self
            outer_self.auth_error = None
            
            class CallbackHandler(BaseHTTPRequestHandler):
                
                def do_GET(self):
                    query = urllib.parse.urlparse(self.path).query
                    params = urllib.parse.parse_qs(query)
                    
                    if 'code' in params:
                        outer_self.auth_code = params['code'][0]
                        self.send_response(200)
                        self.send_header('Content-type', 'text/html; charset=utf-8')
                        self.end_headers()
                        html = """
                        <html><body style="font-family: Arial, sans-serif; text-align: center; padding-top: 50px;">
                            <h2>Authorization completed successfully</h2>
                            <p>You can close this tab and return to the Quickport.</p>
                            <script>window.close();</script>
                        </body></html>
                        """
                        self.wfile.write(html.encode('utf-8'))
                    elif 'error' in params:
                        error_desc = params.get('error_description', ['Unknown authorization error'])[0]
                        outer_self.auth_error = error_desc
                        
                        self.send_response(400)
                        self.send_header('Content-type', 'text/html; charset=utf-8')
                        self.end_headers()
                        
                        html = """
                        <html><body style="font-family: Arial, sans-serif; text-align: center; padding-top: 50px;">
                            <h2>Returning to the application...</h2>
                            <p>You can safely close this tab if it doesn't close automatically.</p>
                            <script>window.close();</script>
                        </body></html>
                        """
                        self.wfile.write(html.encode('utf-8'))
                    else:
                        self.send_response(400)
                        self.end_headers()
                        self.wfile.write(b'Authorization error or missing code.')

                def log_message(self, format, *args):
                    pass
            
            class ReusableHTTPServer(HTTPServer):
                allow_reuse_address = True
            
            server = ReusableHTTPServer(('localhost', self.port), CallbackHandler)
            server.timeout = 1.0 
            max_wait_seconds = 180
            waited = 0

            try:
                webbrowser.open_new(auth_url)
                
                while not self.auth_code and not self.auth_error and waited < max_wait_seconds and not self._is_cancelled:
                    server.handle_request()
                    waited += 1
            finally:
                server.server_close()

            if self._is_cancelled:
                raise Exception('Logging has been canceled by the user.')
            
            if self.auth_error:
                error_msg = urllib.parse.unquote(self.auth_error)
                raise Exception(f'Salesforce authorization error: {error_msg}')
            
            if not self.auth_code:
                raise Exception('Could not get authorization code from Salesforce (Timeout).')
            
            token_url = f'{self.login_url}/services/oauth2/token'
            data = {
                'grant_type': 'authorization_code',
                'client_id': self.client_id,
                'redirect_uri': self.redirect_uri,
                'code': self.auth_code,
                'code_verifier': verifier
            }

            response = requests.post(token_url, data=data)
            
            if response.status_code != 200:
                raise ConnectionError(f'An error occured while downloading tokens: {response.text}')

            tokens = response.json()
            self.login_successful.emit(tokens)
        except Exception as e:
            self.login_failed.emit(str(e))
    

    # get user's name and lastname with access token
    @staticmethod
    def get_user_display_name(identity_url: str, access_token: str) -> str:
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Accept': 'application/json'
        }

        response = requests.get(identity_url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            
            display_name = data.get('display_name')
            if not display_name:
                raise Exception("'display_name' field was found missing from Salesforce response.")
            
            return display_name
        else:
            raise Exception(f'Could not get identity info: {response.text}')