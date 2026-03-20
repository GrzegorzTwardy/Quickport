from PySide6.QtCore import QObject, Signal
from dtos.sf_metadata import SfMetadata

from exceptions.global_exceptions import *


class AppSession(QObject):
    user_logged_in = Signal()
    user_logged_out = Signal()

    def __init__(self):
        super().__init__()
        self.sf_metadata: SfMetadata | None = None


    def login(self, sf_metadata: SfMetadata):
        self.sf_metadata = sf_metadata
        self.user_logged_in.emit()


    def logout(self):
        self.sf_metadata = None
        self.user_logged_out.emit()
        
        
    def validate(self):
        if not self.sf_metadata:
            raise SalesforceDataMissingError('Some data is missing from Salesforce.')

        checks = [
            ('product2_fields', 'Product2'),
            ('pb_entries_fields', 'PricebookEntries'),
            ('pricebooks', 'Pricebook2'),
            ('available_currencies', 'Available Currencies'),
        ]

        for attr, label in checks:
            if not getattr(self.sf_metadata, attr):
                raise SalesforceDataMissingError(f'Missing Salesforce data: {label}')


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