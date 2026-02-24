from uuid import uuid4
from dataclasses import dataclass, field, asdict


@dataclass
class Profile:

    uid: str = field(default_factory=lambda: str(uuid4()), init=False)
    name: str
    production_client_id: str | None
    sandbox_client_id: str | None
    mappers: list[str] # list of paths to mappers
    desc: str


    def to_dict(self):
        return asdict(self)
    
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Profile':
        obj = cls(
            name=data.get('name'),
            production_client_id=data.get('production_client_id'),
            sandbox_client_id=data.get('sandbox_client_id'),
            mappers=data.get('mappers'),
            desc=data.get('desc', ''),
        )
        if 'uid' in data and data['uid'] is not None:
            obj.uid = data['uid']
        return obj