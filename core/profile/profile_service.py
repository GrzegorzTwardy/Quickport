import json
from pathlib import Path
from core.profile.profile_model import Profile
from core.settings.settings_manager import settings_manager


class ProfileService:
    
    PATH_TO_PROFILES = settings_manager.get_setting('profiles_file_path')

    def __init__(self):
        self.profiles: list[Profile] = []
        self.profiles_empty = True

        with open(self.PATH_TO_PROFILES, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.profiles = [Profile.from_dict(p) for p in data]

        if len(self.profiles) != 0:
            self.profiles_empty = False

    
    def _save_to_file(self):   
        with open(self.PATH_TO_PROFILES, 'w', encoding='utf-8') as file:
            json.dump([profile.to_dict() for profile in self.profiles], file, indent=4)
    
    
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
        desc: str,
        primary_key: list
    ):
        for profile in self.profiles:
            if profile.name == name:
                raise ValueError(f"Profile with the name '{name}' already exists.")
        
        profile = Profile(name, production_client_id, sandbox_client_id, desc, primary_key)
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
        desc: str,
        primary_key: list 
    ):
        target_profile = None
        
        for profile in self.profiles:
            if profile.name == name and name != target_profile_name:
                raise ValueError(f"Profile with the name '{name}' already exists.")
            if profile.name == target_profile_name:
                target_profile = profile
            
        if not target_profile:
            raise ValueError(f"Profile '{target_profile_name}' has not been found.")
        
        target_profile.name = name
        target_profile.production_client_id = production_client_id
        target_profile.sandbox_client_id = sandbox_client_id
        target_profile.desc = desc
        target_profile.primary_key = primary_key

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
            
            if len(self.profiles) == 0:
                self.profiles_empty = True
                
            return True
        
        return False


if __name__ == '__main__':
    prof_service = ProfileService()

    # prof_service.add_new_profile(
    #     name='Test Trailblaze Playground',
    #     production_client_id='3MVG9YFqzc_KnL.zP4xDXrq_EmgXWyf0hdCUgCi1fEcFg.GDfYOIC__TDQmQIRDjOMay96.sWNCCKkiq2ECIJ',
    #     sandbox_client_id='',
    #     mappers=[],
    #     desc='test environment'
    # )
    
    prof_service.add_new_profile(
        name='1111111111111111',
        production_client_id='weqwe',
        sandbox_client_id='4324',
        desc='23432324',
        primary_key=['ProductCode']
    )