class SalesforceDataMissingError(Exception):
    
    def __init__(self, data):
        super().__init__(f'Missing Salesforce data: {data}')
        

class ProfileNotFoundError(Exception):
    
    def __init__(self, profile_id):
        super().__init__(f'Profile with id: "{profile_id}" not found')