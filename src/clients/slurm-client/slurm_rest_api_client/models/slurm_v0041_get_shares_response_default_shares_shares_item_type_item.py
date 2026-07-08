from enum import Enum


class SlurmV0041GetSharesResponseDefaultSharesSharesItemTypeItem(str, Enum):
    ASSOCIATION = "ASSOCIATION"
    USER = "USER"

    def __str__(self) -> str:
        return str(self.value)
