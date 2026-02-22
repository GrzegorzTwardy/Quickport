from dataclasses import dataclass

@dataclass
class Credentials:
    access_token: str
    instance_url: str
    refresh_token: str = None