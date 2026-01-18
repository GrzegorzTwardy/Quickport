from uuid import uuid4
from dataclasses import dataclass, field, asdict
from typing import Any
from datetime import date

# dataclasses
@dataclass
class CurrencyMapping:
    
    code: str
    source_column: str | None # moze int
    # mapping_type: str | None
    conversion_factor: float


@dataclass
class PricebookConfig:

    pricebook_id: str
    currencies: list[CurrencyMapping]


@dataclass
class ProductFieldMapping:
    
    included: bool
    sf_target_field: str
    source_column: str | None # moze int
    mapping_type: str | None
    allows_nulls: bool
    args: dict[str, Any] = field(default_factory=dict)


@dataclass
class SheetRule:
    
    sheet_name: str
    # header_row: int
    pricebook_configs: list[PricebookConfig]
    product2_mappings: list[ProductFieldMapping]
    

@dataclass
class MapperModel:
    
    owner_id: str
    sheet_rules: list[SheetRule]
    id: str = field(default_factory=lambda: str(uuid4()), init=False)
    name: str | None = None
    
    def __post_init__(self):
        if not self.name:
            self.name = f'new_mapper_{date.today()}'
        

    def to_dict(self):
        return asdict(self)


    @classmethod
    def from_dict(cls, data: dict) -> "MapperModel":
        return cls(
            owner_id=data["owner_id"],
            sheet_rules=[
                SheetRule(
                    sheet_name=sr["sheet_name"],
                    pricebook_configs=[
                        PricebookConfig(
                            pricebook_id=pb["pricebook_id"],
                            currencies=[
                                CurrencyMapping(**c)
                                for c in pb["currencies"]
                            ],
                        )
                        for pb in sr["pricebook_configs"]
                    ],
                    product2_mappings=[
                        ProductFieldMapping(**pm)
                        for pm in sr["product2_mappings"]
                    ],
                )
                for sr in data["sheet_rules"]
            ],
        )


if __name__ == "__main__":
    model = MapperModel(
        owner_id="user_123",
        sheet_rules=[]
    )
    print(model)
