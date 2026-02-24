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

        self.profiles: list[Profile] = [Profile.from_dict(profile) for profile in self.settings['profiles']]

        if len(self.profiles) != 0:
            self.profiles_empty = False

    
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
        profile = Profile(name, production_client_id, sandbox_client_id, mappers, desc)
        self.profiles.append(profile)

        self.settings['profiles'] = [profile.to_dict() for profile in self.profiles]

        with open(self.PATH_TO_PROFILES, 'w', encoding='utf-8') as file:
            json.dump(self.settings, file, indent=4)


    def add_mapper_to_profile(self, profile_name: str):
        pass


    def edit_profile(self, profile)


if __name__ == '__main__':
    prof_service = ProfileService()

    prof_service.add_new_profile(
        name='Test Trailblaze Playground',
        production_client_id='3MVG9YFqzc_KnL.zP4xDXrq_EmgXWyf0hdCUgCi1fEcFg.GDfYOIC__TDQmQIRDjOMay96.sWNCCKkiq2ECIJ',
        sandbox_client_id='',
        mappers=[],
        desc='test environment'
    )