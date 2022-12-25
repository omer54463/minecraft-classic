from ctypes import c_char, c_ubyte
from typing import Any
from minecraft_classic.opcode import Opcode
from minecraft_classic.packet import Packet
from minecraft_classic.protocol_version import ProtocolVersion


class LoginPacket(Packet):
    opcode_int: int
    protocol_version_int: int
    username: bytes
    password: bytes
    use_cpe_int: int

    _fields_ = [
        ("opcode_int", c_ubyte),
        ("protocol_version_int", c_ubyte),
        ("username", c_char * 0x40),
        ("password", c_char * 0x40),
        ("use_cpe_int", c_ubyte),
    ]

    @property
    def opcode(self) -> Opcode:
        return Opcode(self.opcode_int)

    @opcode.setter
    def opcode(self, opcode: Opcode) -> None:
        self.opcode_int = opcode.value

    @property
    def protocol_version(self) -> ProtocolVersion:
        return ProtocolVersion(self.protocol_version_int)

    @protocol_version.setter
    def protocol_version(self, protocol_version: ProtocolVersion) -> None:
        self.protocol_version_int = protocol_version.value

    @property
    def use_cpe(self) -> bool:
        return self.use_cpe_int == 0x42

    @use_cpe.setter
    def use_cpe(self, use_cpe: bool) -> None:
        self.use_cpe_int = 0x42 if use_cpe else 0x00
