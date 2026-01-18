from dataclasses import dataclass, field

from utils.security import salt
from utils.creds_model import Credentials


@dataclass
class Profile:
    uname: str
    login: str
    password_hash: str
    token: str
    api_key: str
    url_instance: str
    parsers: list
    desc: str
    salt: str = field(default_factory=lambda: salt(10))

    @classmethod
    def from_creds(cls, creds: Credentials):
        return cls(
            uname=creds.uname,
            login=creds.login,
            password_hash=creds.password_hash,
            token=creds.token,
            api_key=creds.api_key,
            url_instance=creds.url_instance,
            parsers=creds.parsers,
            desc=creds.desc
        )

    def get(self):
        return {
            'uname': self.uname,
            'login': self.login,
            'parssword_hash': self.password_hash,
            'salt': self.salt,
            'token': self.token,
            'api_key': self.api_key,
            'url_instance': self.url_instance,
            'parsers': self.parsers,
            'desc': self.desc
        }
