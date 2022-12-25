from ctypes import c_char, c_ubyte
from minecraft_classic.opcode import Opcode
from minecraft_classic.packet import Packet


class MessagePacket(Packet):
    opcode_int: int
    player_id: int
    text: bytes

    _fields_ = [
        ("opcode_int", c_ubyte),
        ("player_id", c_ubyte),
        ("text", c_char * 0x40),
    ]

    @property
    def opcode(self) -> Opcode:
        return Opcode(self.opcode_int)

    @opcode.setter
    def opcode(self, opcode: Opcode) -> None:
        self.opcode_int = opcode.value
