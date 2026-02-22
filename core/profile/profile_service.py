import json
from pathlib import Path
from core.profile.profile_model import Profile


class ProfileService:
    
    PATH_TO_PROFILES = Path('../../profiles/')
    
    def get_profile_by_name(self, name: str) -> Profile:
        for json_file in self.PATH_TO_PROFILES.glob('*.json'):
            profile = Profile.from_json(json_file)
            if profile.profile_name == name:
                return profile
        return None
    
    def get_all_profiles(self) -> list[Profile]:
        profiles = []
        for json_file in self.PATH_TO_PROFILES.glob('*.json'):
            profile = Profile.from_json(json_file)
            profiles.append(profile)
        return profiles
    
    def add_new_profile(
        self,
        profile_name: str,
        instance_url: str,
        consumer_key: str,
        desc: str
    ):
        profile = Profile(
            profile_name=profile_name,
            instance_url=instance_url,
            consumer_key=consumer_key,
            mappers=[],
            desc=desc
        )
        
        with open(self.PATH_TO_PROFILES, 'w', encoding='utf-8') as file:
            pass