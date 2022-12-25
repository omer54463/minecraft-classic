from __future__ import annotations
from ctypes import c_ubyte
from typing import BinaryIO
from minecraft_classic.opcode import Opcode
from minecraft_classic.packet import Packet


class LevelBeginPacket(Packet):
    opcode_int: int
    world_size_be: bytes

    _fields_ = [
        ("opcode_int", c_ubyte),
        ("world_size_be", c_ubyte * 4),
    ]

    @property
    def opcode(self) -> Opcode:
        return Opcode(self.opcode_int)

    @opcode.setter
    def opcode(self, opcode: Opcode) -> None:
        self.opcode_int = opcode.value

    @property
    def world_size(self) -> int:
        return int.from_bytes(self.world_size_be, byteorder="big")

    @world_size.setter
    def world_size(self, world_size: int) -> None:
        self.world_size_be = world_size.to_bytes(
            len(self.world_size_be),
            byteorder="big",
        )
