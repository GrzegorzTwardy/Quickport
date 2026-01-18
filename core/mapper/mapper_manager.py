# Allows creating, editing and removing mapper models
# used by mapper_window_controller.py

import json
# from core.mapper.mapper_manager import dict_to_mapper, mapper_to_dict
from core.mapper.mapper_model import MapperModel

MAPPERS_PATH = '../mappers/'

class MapperManager:

    def __init__(self, gui_obj):
        self.gui_obj = gui_obj
        self.managed_mapper = None # mapperModel
    
    # === MAPPER CRUD ===
    def get_mappers(self):
        try:
            with open(MAPPERS_PATH, 'r') as file:
                mappers = json.load(file)
                return mappers
        except FileNotFoundError:
            print('File with mappers not found.')
        

    def create_new_mapper(self) -> MapperModel:
        self.managed_mapper = MapperModel.new()
        
    
    # user clicks "Save" in mapper editor and code below executes:
    def save_mapper(self):
        mapper_dict = mapper_to_dict(self.managed_mapper)
        updated = False
        mappers = self.get_mappers()
        
        for i, p in mappers:
            if p["id"] == mapper_dict["id"]:
                p[i] = mapper_dict
                updated = True
                break
        
        if not updated:
            mappers.append(mapper_dict)
        
        with open(MAPPERS_PATH, 'w') as file:
            json.dump(mappers, file)

    