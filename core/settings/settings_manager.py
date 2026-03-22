# singleton module (settings_manager)
import os
import json
from pathlib import Path
from exceptions.global_exceptions import *

default_values = {
    'mappers_path': './mappers/', # shouldn't be changed
    'output_path': './output/',
    'profiles_file_path': './profiles.json', # shouldn't be changed
    'max_table_records': 50
}

class SettingsManager:

    AVAILABLE_SETTINGS = ['mappers_path', 'output_path', 'profiles_file_path', 'max_table_records']

    def __init__(self, path='./settings.json'):
        self.path = path
        self.settings = default_values.copy()


    def _save_settings(self):
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(self.settings, file, indent=4)
     
    
    def _ensure_paths_exist(self):
        directories_to_check = ['mappers_path', 'output_path']
        for dir_name in directories_to_check:
            dir_path = Path(self.get_setting(dir_name))
            if not dir_path.exists():
                try:
                    dir_path.mkdir(parents=True, exist_ok=True)
                except Exception as e:
                    raise SettingsError(f'Critical error: Cannot create directory {dir_path}. Reason:\n{e}')
        
        profiles_path = Path(self.get_setting('profiles_file_path'))
        if not profiles_path.exists():
            try:
                profiles_path.parent.mkdir(parents=True, exist_ok=True)
                
                with open(profiles_path, 'w', encoding='utf-8') as file:
                    json.dump([], file, indent=4)
            except Exception as e:
                raise SettingsError(f'Critical error: Cannot create file {profiles_path}. Reason:\n{e}')
    
    
    def load_settings(self):
        try:
            if os.path.exists(self.path) and os.path.getsize(self.path) > 0:
                with open(self.path, 'r', encoding='utf-8') as file:
                    loaded_settings = json.load(file)
                    
                if not loaded_settings:
                    raise ValueError("Empty settings")
                    
                self.settings.update(loaded_settings)
            else:
                raise FileNotFoundError

        except (json.JSONDecodeError, FileNotFoundError, ValueError):
            self._save_settings()
            
        self._ensure_paths_exist()
     
            
    def _save_settings(self):
        with open(self.path, 'w', encoding='utf-8') as file:
            json.dump(self.settings, file, indent=4)
        
            
    def change_setting(self, setting_name: str, value: str):
        if setting_name not in self.AVAILABLE_SETTINGS:
            raise ValueError(f'Unknown setting: {setting_name}')
        
        match setting_name:
            case 'mappers_path' | 'output_path' | 'profiles_file_path':
                self.settings[setting_name] = str(Path(value))
            case 'max_table_records':
                try:
                    self.settings[setting_name] = int(value)
                except ValueError:
                    self.settings[setting_name] = 50
            case _:
                self.settings[setting_name] = value
            
        self._save_settings()
        
        
    def get_setting(self, setting_name: str, default=None):
        if setting_name not in self.AVAILABLE_SETTINGS:
            raise ValueError(f'Unknown setting: {setting_name}')
            
        return self.settings.get(setting_name, default_values[setting_name])
    
    
    def get_all_settings(self):
        return self.settings.copy()
    

    def reset_settings(self):
        self.settings = default_values.copy()
        self._save_settings()
        

settings_manager = SettingsManager()
settings_manager.load_settings()
    

if __name__ == '__main__':
    
    settings_manager.change_setting('mappers_path', './mappers/')
    # settings_manager.change_setting('max_table_records', '50')
    # print(settings_manager.get_setting('max_table_records'))