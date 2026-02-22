import json
from dataclasses import dataclass


@dataclass
class Profile:
    
    profile_name: str
    instance_url: str
    consumer_key: str
    mappers: list
    desc: str
    
     
    @classmethod
    def from_json(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            pr = json.load(file)

        return cls(
            profile_name=pr.get('profile_name'),
            instance_url=pr.get('instance_url'),
            consumer_key=pr.get('consumer_key'),
            mappers=pr.get('mappers', []),
            desc=pr.get('desc', "")
        )
        

    def get(self):
        return {
            'profile_name': self.profile_name,
            'instance_url': self.instance_url,
            'consumer_key': self.consumer_key,
            'mappers': self.mappers,
            'desc': self.desc
        }
