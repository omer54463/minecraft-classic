from ctypes import c_char, c_ubyte
from typing import Any
from minecraft_classic.opcode import Opcode
from minecraft_classic.packet import Packet


class ExtEntryPacket(Packet):
    opcode_int: int
    name: bytes
    version_be: bytes

    _fields_ = [
        ("opcode_int", c_ubyte),
        ("name", c_char * 0x40),
        ("version_be", c_ubyte * 0x4),
    ]

    @property
    def opcode(self) -> Opcode:
        return Opcode(self.opcode_int)

    @opcode.setter
    def opcode(self, opcode: Opcode) -> None:
        self.opcode_int = opcode.value

    @property
    def version(self) -> int:
        return int.from_bytes(self.version_be, byteorder="big")

    @version.setter
    def version(self, ext_version: int) -> None:
        self.version_be = ext_version.to_bytes(
            len(self.version_be),
            byteorder="big",
        )
