from PySide6.QtCore import QObject, Signal
from dtos.sf_metadata import SfMetadata

from exceptions.global_exceptions import *


class AppSession(QObject):
    user_logged_in = Signal()
    user_logged_out = Signal()

    def __init__(self):
        super().__init__()
        self.is_authenticated: bool = False
        self.user_id: str | None = None
        self.sf_metadata: SfMetadata | None = None


    def login(self, user_id: str, sf_metadata: SfMetadata):
        self.user_id = user_id
        self.sf_metadata = sf_metadata
        self.is_authenticated = True
        self.user_logged_in.emit()


    def logout(self):
        self.user_id = None
        self.sf_metadata = None
        self.is_authenticated = False
        self.user_logged_out.emit()
        
        
    def validate(self):
        if not self.user_id:
            raise ProfileNotFoundError(self.user_id)

        if not self.sf_metadata:
            raise SalesforceDataMissingError('Couldn\'t load data from Salesforce')

        checks = [
            ('product2_fields', 'Product2'),
            ('pb_entries_fields', 'PricebookEntries'),
            ('pricebooks', 'Pricebook2'),
            ('available_currencies', 'Available Currencies'),
        ]

        for attr, label in checks:
            if not getattr(self.sf_metadata, attr):
                raise SalesforceDataMissingError(label)


    def test_login(self):
        def fields_to_dict(fields):
            return {
                field: {
                    'required': True,
                    'readOnly': False
                }
                for field in fields
            }
        
        self.login(
            user_id='343243242',
            sf_metadata=SfMetadata(
                product2_fields=fields_to_dict(['name', 'SKU', 'manu', 'category', 'desc', 'a-really-long-field-name-123-2321-231']),
                pb_entries_fields=fields_to_dict(['PricebookId', 'Product2Id', 'UnitPrice', 'IsActive']),
                pricebooks={
                    'id0934':'pb-1', 
                    'id3742':'pb-2', 
                    'id3321':'pb-3', 
                    'id3764':'new_pb_1'
                },
                available_currencies=['EUR', 'PLN', 'USD', 'CZK', 'JPY', 'GBP']
            )
        )