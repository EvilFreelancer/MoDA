from dataclasses import dataclass
from typing import Literal

Role = Literal["system", "user", "assistant", "function-call", "function-response"]


@dataclass
class Message:
    role: Role
    content: str
    masked: bool = False
    ipython: bool = False
    eot: bool = True

    @classmethod
    def from_dict(cls, d: dict) -> "Message":
        return cls(
            role=d["role"],
            content=d["content"],
            masked=d.get("masked", False),
            ipython=d.get("ipython", False),
            eot=d.get("eot", True),
        )
