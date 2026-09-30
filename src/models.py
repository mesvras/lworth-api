from dataclasses import dataclass


@dataclass
class User:
    username: str
    password_hash: str
    id: int | None = None
