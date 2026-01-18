import os
import json
from core.profile.profile_model import Profile
from utils.creds_model import Credentials

class ProfileService:
    
    path = 'profiles/storage/profiles.json'
    
    def get_profile(self, uname):
        with open(self.path, 'r') as file:
            profiles = json.load(file)
            for p in profiles:
                if p["uname"] == uname:
                    return p
        return None
    
    
    def get_profiles(self):
        with open(self.path, 'r') as file:
            profiles = json.load(file)
            return profiles
            
    
    def add_profile(self, profile):      
        if not os.path.exists(self.path):
            profiles = []
        else:
            with open(self.path, 'r') as file:
                profiles = json.load(file)
                
        profiles.append(profile.get())

        with open(self.path, 'w') as file:
            json.dump(profiles, file, indent=4)
            
            
    def remove_profile(self, uname):
        if not os.path.exists(self.path):
            print('There are no profiles to delete.')
        else:
            with open(self.path, 'r') as file:
                profiles = json.load(file)
                
        for i in range(len(profiles)):
            if profiles[i]['uname'] == uname:
                print(f'removing {uname}\'s profile')
                del profiles[i]
                break

        with open(self.path, 'w') as file:
            json.dump(profiles, file, indent=4)
            
            
    def edit_profile(self, uname, changes): # 'changes' is a dict
        if not os.path.exists(self.path):
            print(f'Profile "{uname}" has not been found.')
        else:
            with open(self.path, 'r') as file:
                profiles = json.load(file)
                
        for i in range(len(profiles)):
            if profiles[i]['uname'] == uname:
                for attr in changes:
                    profiles[i][attr] = changes[attr] 
                break

        with open(self.path, 'w') as file:
            json.dump(profiles, file, indent=4)
            
    
if __name__ == "__main__":
    
    choice = input('Choose (1-add+edit, 2-remove, 3-get): ')
    prof_service = ProfileService()
    
    if choice == '1':
        creds = Credentials('s', 's', 's', 's', 's', 's', 's', [], 's')
        prof = Profile(creds)
        prof_service.add_profile(prof)
        print('profile added')
        
        changes = {
            'uname': 'newname',
            'parsers': ['new_parser']
        }
        
        prof_service.edit_profile('s', changes)
        print('profile\'s been edited')
        
    elif choice == '2':
        prof_service.remove_profile('newname')
    elif choice == '3':
        p1 = prof_service.get_profile('newname')
        all_p = prof_service.get_profiles()
        print(p1)
        print(all_p)
    else:
        print('wrong choice.')