class MappingError(Exception):
    pass
        

class PricebookLoadError(Exception):
    
    def __init__(self, pb_file):
        super().__init__(f'Couldn\'t load pricebooks from "{pb_file}".')
        
        
class MapperLoadError(Exception):
    
    def __init__(self, mapper_file):
        super().__init__(f'An error has occured while loading mapper "{mapper_file}".')


class SheetNotFoundError(Exception):
    
    def __init__(self, sheet_name):
        super().__init__(f'Sheet "{sheet_name}" has not been found')


class SourceColumnNotFoundError(Exception):
    
    def __init__(self, sheet_name, column, sf_field):
        super().__init__(
            f'Column "{column}" not found in sheet "{sheet_name}".'
            f'(mapping to SF field "{sf_field}")'
        )
        
class UnknownMappingTypeError(Exception):
    
    def __init__(self, mapping_type):
        super().__init__(f'Uknown mapping type found in mapper file: "{mapping_type}".')
        

class TargetSfFieldNotFoundError(Exception):
    
    def __init__(self, field):
        super().__init__(f'Mapper file defines Salesforce object\'s field "{field}" that doesn\'t exist in Salesforce.')