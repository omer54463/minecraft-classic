from ctypes import c_char, c_ubyte
from typing import Any
from minecraft_classic.opcode import Opcode
from minecraft_classic.packet import Packet


class ExtInfoPacket(Packet):
    opcode_int: int
    exts_count_be: bytes

    _fields_ = [
        ("opcode", c_ubyte),
        ("server_name", c_char * 0x40),
        ("exts_count_be", c_ubyte * 0x2),
    ]

    @property
    def opcode(self) -> Opcode:
        return Opcode(self.opcode_int)

    @opcode.setter
    def opcode(self, opcode: Opcode) -> None:
        self.opcode_int = opcode.value

    @property
    def exts_count(self) -> int:
        return int.from_bytes(self.exts_count_be, byteorder="big")

    @exts_count.setter
    def exts_count(self, exts_count: int) -> None:
        self.exts_count_be = exts_count.to_bytes(
            len(self.exts_count_be),
            byteorder="big",
        )
