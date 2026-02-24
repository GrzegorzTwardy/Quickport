import json
from pathlib import Path
from core.profile.profile_model import Profile
from core.mapper.mapper_model import MapperModel


class ProfileService:
    
    PATH_TO_PROFILES = Path('./settings.json')

    def __init__(self):
        self.settings = None
        self.profiles = []
        self.profiles_empty = True

        with open(self.PATH_TO_PROFILES, 'r', encoding='utf-8') as settings_file:
            self.settings = json.load(settings_file)

        if not self.settings:
            raise FileNotFoundError('Missing settings file.')

        profiles_data = self.settings.get('profiles', [])
        self.profiles: list[Profile] = [Profile.from_dict(profile) for profile in profiles_data]

        if len(self.profiles) != 0:
            self.profiles_empty = False

    
    def _save_to_file(self):
        self.settings['profiles'] = [profile.to_dict() for profile in self.profiles]
        
        with open(self.PATH_TO_PROFILES, 'w', encoding='utf-8') as file:
            json.dump(self.settings, file, indent=4)
    
    
    def get_profile_by_name(self, name: str) -> Profile | None:
        for profile in self.profiles:
            if profile.name == name:
                return profile
        return None

    
    def get_all_profiles(self) -> list[Profile]:
        return self.profiles
    

    def add_new_profile(
        self,
        name: str,
        production_client_id: str,
        sandbox_client_id: str | None,
        mappers: list[MapperModel],
        desc: str
    ):
        # check if name is not already taken
        for profile in self.profiles:
            if profile.name == name:
                raise ValueError(f"Profile with the name '{name}' already exists.")
        
        profile = Profile(name, production_client_id, sandbox_client_id, mappers, desc)
        self.profiles.append(profile)
        self.profiles_empty = False
        
        self._save_to_file()


    def add_mapper_to_profile(self, profile_name: str):
        pass


    def edit_profile(
        self,
        target_profile_name: str,
        name: str,
        production_client_id: str,
        sandbox_client_id: str | None,
        mappers: list[MapperModel],
        desc: str
    ):
        target_profile = None
        
        for profile in self.profiles:
            # if new profile name is aready taken with exception to the profile that is being edited (initially it must have the same name)
            if profile.name == name and name != target_profile_name:
                raise ValueError(f"Profile with the name '{name}' already exists.")
            if profile.name == target_profile_name:
                target_profile = profile
            
        if not target_profile:
            raise ValueError(f"Profile '{target_profile_name}' has not been found.")
        
        target_profile.name = name
        target_profile.production_client_id = production_client_id
        target_profile.sandbox_client_id = sandbox_client_id
        target_profile.mappers = mappers
        target_profile.desc = desc

        self._save_to_file()
            
    
    def remove_profile(self, profile_name: str) -> bool:
        target_profile = None
    
        for profile in self.profiles:
            if profile.name == profile_name:
                target_profile = profile
                break
            
        if target_profile:
            self.profiles.remove(target_profile)
            self._save_to_file()
            return True
        
        return False


if __name__ == '__main__':
    prof_service = ProfileService()

    prof_service.add_new_profile(
        name='Test Trailblaze Playground',
        production_client_id='3MVG9YFqzc_KnL.zP4xDXrq_EmgXWyf0hdCUgCi1fEcFg.GDfYOIC__TDQmQIRDjOMay96.sWNCCKkiq2ECIJ',
        sandbox_client_id='',
        mappers=[],
        desc='test environment'
    )