from enum import Enum


class V0039JobInfoPowerFlagsItem(str, Enum):
    EQUAL_POWER = "EQUAL_POWER"

    def __str__(self) -> str:
        return str(self.value)
