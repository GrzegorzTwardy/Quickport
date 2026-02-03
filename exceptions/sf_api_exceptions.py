class SalesforceApiError(Exception):
    pass


class SalesforceJobFailedError(Exception):
    pass


class MissingRequiredColumnError(Exception):
    pass


class InvalidCsvColumnNamesError(Exception):
    
    def __init__(self, names, obj: str):
        names_str = ''
        for n in names:
            names_str += f' {n}'
        super().__init__(f'Source file contains fields: "{names_str}" that do not exist in {obj} object.')