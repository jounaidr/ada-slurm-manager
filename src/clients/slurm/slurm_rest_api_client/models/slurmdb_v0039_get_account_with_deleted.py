from enum import Enum


class SlurmdbV0039GetAccountWithDeleted(str, Enum):
    FALSE = "false"
    TRUE = "true"

    def __str__(self) -> str:
        return str(self.value)
