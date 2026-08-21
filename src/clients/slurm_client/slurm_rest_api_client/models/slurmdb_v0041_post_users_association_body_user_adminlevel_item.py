from enum import Enum


class SlurmdbV0041PostUsersAssociationBodyUserAdminlevelItem(str, Enum):
    ADMINISTRATOR = "Administrator"
    NONE = "None"
    NOT_SET = "Not Set"
    OPERATOR = "Operator"

    def __str__(self) -> str:
        return str(self.value)
