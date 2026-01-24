from dataclasses import dataclass

# save data from API to this
@dataclass
class SfMetadata:
    
    # product2_fields: list[str]
    # pb_entries_fields: list[str]
    product2_fields: dict[str: dict]
    pb_entries_fields: dict[str: dict]
    pricebooks: dict[str, str] # id, name
    available_currencies: list[str]
