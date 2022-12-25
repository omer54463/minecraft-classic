from enum import Enum


class ProtocolVersion(Enum):
    value: int

    VERSION_0017 = 4
    VERSION_0019 = 5
    VERSION_0020 = 6
    VERSION_0030 = 7
