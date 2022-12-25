from ctypes import c_char, c_ubyte
from minecraft_classic.opcode import Opcode
from minecraft_classic.packet import Packet


class AddEntityPacket(Packet):
    opcode_int: int
    player_id: int
    player_name: bytes
    x_be: bytes
    y_be: bytes
    z_be: bytes
    yaw: int
    pitch: int

    _fields_ = [
        ("opcode_int", c_ubyte),
        ("player_id", c_ubyte),
        ("player_name", c_char * 0x40),
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
