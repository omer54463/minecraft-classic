from __future__ import annotations
from ctypes import c_ubyte
from typing import BinaryIO
from minecraft_classic.opcode import Opcode
from minecraft_classic.packet import Packet


class EntityTeleportPacket(Packet):
    opcode_int: int
    held_block_be: bytes
    x_be: bytes
    y_be: bytes
    z_be: bytes
    yaw: int
    pitch: int

    _fields_ = [
        ("opcode_int", c_ubyte),
        ("held_block_be", c_ubyte * 0x1),
        ("x_be", c_ubyte * 0x2),
        ("y_be", c_ubyte * 0x2),
        ("z_be", c_ubyte * 0x2),
        ("yaw", c_ubyte),
        ("pitch", c_ubyte),
    ]

    @property
    def opcode(self) -> Opcode:
        return Opcode(self.opcode_int)

    @opcode.setter
    def opcode(self, opcode: Opcode) -> None:
        self.opcode_int = opcode.value

    @property
    def held_block(self) -> int:
        return int.from_bytes(self.held_block_be, byteorder="big")

    @held_block.setter
    def held_block(self, held_block: int) -> None:
        self.held_block_be = held_block.to_bytes(
            len(self.held_block_be),
            byteorder="big",
        )

    @property
    def x(self) -> int:
        return int.from_bytes(self.x_be, byteorder="big")

    @x.setter
    def x(self, x: int) -> None:
        self.x_be = x.to_bytes(
            len(self.x_be),
            byteorder="big",
        )

    @property
    def y(self) -> int:
        return int.from_bytes(self.y_be, byteorder="big")

    @y.setter
    def y(self, y: int) -> None:
        self.y_be = y.to_bytes(
            len(self.y_be),
            byteorder="big",
        )

    @property
    def z(self) -> int:
        return int.from_bytes(self.z_be, byteorder="big")

    @z.setter
    def z(self, z: int) -> None:
        self.z_be = z.to_bytes(
            len(self.z_be),
            byteorder="big",
        )
