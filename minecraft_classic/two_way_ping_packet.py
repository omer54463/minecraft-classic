from ctypes import c_ubyte
from minecraft_classic.opcode import Opcode
from minecraft_classic.packet import Packet


class TwoWayPingPacket(Packet):
    opcode_int: int
    server_to_client_int: int
    value_be: bytes

    _fields_ = [
        ("opcode_int", c_ubyte),
        ("server_to_client_int", c_ubyte),
        ("value_be", c_ubyte * 2),
    ]

    @property
    def opcode(self) -> Opcode:
        return Opcode(self.opcode_int)

    @opcode.setter
    def opcode(self, opcode: Opcode) -> None:
        self.opcode_int = opcode.value

    @property
    def server_to_client(self) -> bool:
        return self.server_to_client_int == 1

    @server_to_client.setter
    def server_to_client(self, server_to_client: bool) -> None:
        self.server_to_client_int = 1 if server_to_client else 0

    @property
    def value(self) -> int:
        return int.from_bytes(self.value_be, byteorder="big")

    @value.setter
    def value(self, value: int) -> None:
        self.value_be = value.to_bytes(
            len(self.value_be),
            byteorder="big",
        )
