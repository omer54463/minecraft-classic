from __future__ import annotations
from ctypes import c_ubyte
from typing import BinaryIO
from minecraft_classic.opcode import Opcode
from minecraft_classic.packet import Packet


class LevelDataPacket(Packet):
    opcode_int: int
    chunk_length_be: bytes
    chunk_data: bytes
    percent_complete: int

    _fields_ = [
        ("opcode_int", c_ubyte),
        ("chunk_length_be", c_ubyte * 0x2),
        ("chunk_data", c_ubyte * 0x400),
        ("percent_complete", c_ubyte),
    ]

    @property
    def opcode(self) -> Opcode:
        return Opcode(self.opcode_int)

    @opcode.setter
    def opcode(self, opcode: Opcode) -> None:
        self.opcode_int = opcode.value

    @property
    def chunk_length(self) -> int:
        return int.from_bytes(self.chunk_length_be, byteorder="big")

    @chunk_length.setter
    def chunk_length(self, chunk_length: int) -> None:
        self.chunk_length_be = chunk_length.to_bytes(
            len(self.chunk_length_be),
            byteorder="big",
        )
