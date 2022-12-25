from ctypes import c_ubyte
from minecraft_classic.opcode import Opcode
from minecraft_classic.packet import Packet


class CustomBlockLevelPacket(Packet):
    opcode_int: int

    _fields_ = [
        ("opcode_int", c_ubyte),
        ("value", c_ubyte),
    ]

    @property
    def opcode(self) -> Opcode:
        return Opcode(self.opcode_int)

    @opcode.setter
    def opcode(self, opcode: Opcode) -> None:
        self.opcode_int = opcode.value
