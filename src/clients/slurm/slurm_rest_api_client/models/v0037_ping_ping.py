from enum import Enum


class V0037PingPing(str, Enum):
    DOWN = "DOWN"
    UP = "UP"

    def __str__(self) -> str:
        return str(self.value)
