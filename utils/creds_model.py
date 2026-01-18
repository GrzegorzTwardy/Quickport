from dataclasses import dataclass

@dataclass
class Credentials:
    uname: str
    login: str
    password_hash: str
    salt: str
    token: str
    api_key: str
    url_instance: str
    parsers: list
    desc: str
