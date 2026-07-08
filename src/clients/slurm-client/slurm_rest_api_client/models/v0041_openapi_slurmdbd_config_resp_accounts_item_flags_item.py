from enum import Enum


class V0041OpenapiSlurmdbdConfigRespAccountsItemFlagsItem(str, Enum):
    DELETED = "DELETED"
    NOUSERSARECOORDS = "NoUsersAreCoords"
    USERSARECOORDS = "UsersAreCoords"
    WITHASSOCIATIONS = "WithAssociations"
    WITHCOORDINATORS = "WithCoordinators"

    def __str__(self) -> str:
        return str(self.value)
