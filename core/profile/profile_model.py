import json
from dataclasses import dataclass, field
from utils.security import salt
from utils.creds_model import Credentials


@dataclass
class Profile:
    
    uname: str
    password: str
    security_token: str
    consumer_key: str
    consumer_secret: str
    instance_url: str
    # parsers: list
    # desc: str
    # salt: str = field(default_factory=lambda: salt(10))
     
    @classmethod
    def from_json(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            pr = json.load(file)
        return cls(
            uname=pr['username'],
            password=pr['password'],
            security_token=pr['security_token'],
            consumer_key=pr['consumer_key'],
            consumer_secret=pr['consumer_secret'],
            instance_url=pr['instance_url']
        )
        

    def get(self):
        return {
            'uname': self.uname,
            'login': self.login,
            'parssword': self.password,
            'salt': self.salt,
            'token': self.token,
            'api_key': self.api_key,
            'instance_url': self.instance_url,
            'parsers': self.parsers,
            'desc': self.desc
        }
