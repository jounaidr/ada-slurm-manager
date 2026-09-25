from enum import Enum


class V0039JobFlagsItem(str, Enum):
    CLEAR_SCHEDULING = "CLEAR_SCHEDULING"
    NONE = "NONE"
    NOT_SET = "NOT_SET"
    STARTED_ON_BACKFILL = "STARTED_ON_BACKFILL"
    STARTED_ON_SCHEDULE = "STARTED_ON_SCHEDULE"
    STARTED_ON_SUBMIT = "STARTED_ON_SUBMIT"

    def __str__(self) -> str:
        return str(self.value)
