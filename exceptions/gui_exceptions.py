class MappingNotSetError(Exception):
    def __init__(self, data):
        self.data = data
        super().__init__(f'Mapping for "{self.data}" has to be set.')