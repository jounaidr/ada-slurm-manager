from enum import Enum


class V0038Signal(str, Enum):
    ABRT = "ABRT"
    ALRM = "ALRM"
    CONT = "CONT"
    HUP = "HUP"
    INT = "INT"
    KILL = "KILL"
    QUIT = "QUIT"
    STOP = "STOP"
    TERM = "TERM"
    TSTP = "TSTP"
    TTIN = "TTIN"
    TTOU = "TTOU"
    URG = "URG"
    USR1 = "USR1"
    USR2 = "USR2"

    def __str__(self) -> str:
        return str(self.value)
