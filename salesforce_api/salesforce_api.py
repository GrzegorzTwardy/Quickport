import requests
from dtos.session import AppSession
from dtos.sf_metadata import SfMetadata
from core.profile.profile_model import Profile
from requests.exceptions import RequestException
from simple_salesforce import Salesforce


class SalesforceApi:
    
    def __init__(self, profile: Profile):
        self.sf = None
        self.username = profile.uname
        self.password = profile.password
        self.security_token = profile.security_token
        self.consumer_key = profile.consumer_key
        self.consumer_secret = profile.consumer_secret
        self.instance_url = profile.instance_url

        # SF Objects
        self.standard_pricebook_dict = {} # id: name
        self.custom_pricebooks_dict = {} # id: name

    def connect(self) -> Salesforce:
        url = f"{self.instance_url}/services/oauth2/token"

        data = {
            "grant_type": "password",
            "client_id": self.consumer_key,
            "client_secret": self.consumer_secret,
            "username": self.username,
            "password": f"{self.password}{self.security_token}",
        }

        try:
            response = requests.post(url, data=data, timeout=15)
            response.raise_for_status() # !200 => exception
            payload = response.json()

            if 'access_token' not in payload or 'instance_url' not in payload:
                raise ValueError(f'Invalid OAuth response: {payload}')

            token = payload['access_token']
            instance = payload['instance_url']

            self.sf = Salesforce(instance_url=instance, session_id=token)
            print('Connection with Salesforce established.')
            
        except RequestException as e:
            print('Error: Couldn\'nt connect with Salesforce API.')
            print(str(e))
            raise
        except ValueError as e:
            print('Error: Invalid server response.')
            print(str(e))
            raise
        except Exception as e:
            print('Unexpected Error.')
            print(str(e))
            raise
        
    # === fetching Salesforce Objects === 
    def get_prod2_fields(self):
        desc = self.sf.Product2.describe()
        field_names = [f['name'] for f in desc['fields']]
        return field_names
    
    
    def get_pb_entry_fields(self):
        desc = self.sf.PricebookEntry.describe()
        field_names = [f['name'] for f in desc['fields']]
        return field_names
    
    
    def load_all_pricebooks(self):
        # custom pricebooks (Pricebook2)
        custom_records = self.sf.query_all("""
            SELECT Id, Name
            FROM Pricebook2
            WHERE IsActive = true
            AND IsStandard = false
            ORDER BY Name ASC
        """) 
        self.custom_pricebooks_dict = { row['Id']: row['Name'] for row in custom_records['records'] } 
        
        # Standard Pricebook
        standard_records = self.sf.query("""
            SELECT Id, Name
            FROM Pricebook2
            WHERE IsStandard = true
        """)
        self.standard_pricebook_dict = {
            row['Id']: row['Name'] for row in standard_records['records'] 
        }
        print('Pricebooks loaded.')
    
    
    def get_available_currencies(self):
        result = self.sf.query("SELECT IsoCode FROM CurrencyType WHERE IsActive = true")
        return [row["IsoCode"] for row in result["records"]]

    
    def get_user_sf_metadata(self):        
        self.load_all_pricebooks()
        return SfMetadata(
            product2_fields=self.get_prod2_fields(),
            pb_entries_fields=self.get_pb_entry_fields(),
            pricebooks=self.custom_pricebooks_dict,
            available_currencies=self.get_available_currencies()
        )
    
    
if __name__ == '__main__':
    profile = Profile.from_json('./cert/test_creds.json')    
    api = SalesforceApi(profile)
    api.connect()
    print(api.get_user_sf_metadata())