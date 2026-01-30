class MappingError(Exception):
    pass
        
class PricebookLoadError(Exception):
    pass
        
class MapperLoadError(Exception):
    pass

class SheetNotFoundError(Exception):
    pass

class SourceColumnNotFoundError(Exception):
    pass     
        
class UnknownMappingTypeError(Exception):
    pass    

class TargetSfFieldNotFoundError(Exception):
    pass