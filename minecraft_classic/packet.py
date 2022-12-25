from ctypes import Structure, sizeof
from typing import Any, BinaryIO, TypeVar

PacketType = TypeVar("PacketType", bound="Packet")


class Packet(Structure):
    _fields_: list[tuple[str, type[Any]]]

    @classmethod
    def parse(cls: type[PacketType], data: bytes) -> tuple[PacketType, bytes]:
        return cls.from_buffer_copy(data), data[sizeof(cls) :]

    def pretty(self, indent: int = 0) -> str:
        result = ""

        result += "\t" * indent
        result += f"{type(self).__name__} {{\n"

        for field_name, *_ in self._fields_:
            if field_name.endswith("_be"):
                field_name = field_name[: -len("_be")]
            elif field_name.endswith("_int"):
                field_name = field_name[: -len("_int")]

            field_value = getattr(self, field_name)
            if isinstance(field_value, Packet):
                value_string = field_value.pretty(indent + 1)
            elif isinstance(field_value, int):
                value_string = hex(field_value)
            else:
                value_string = str(field_value)

            result += "\t" * (indent + 1)
            result += f"{type(field_value).__name__} {field_name} = {value_string}"
            result += "\n"

        result += "\t" * indent
        result += "}"

        return result

    def __str__(self) -> str:
        return self.pretty()

    def __repr__(self) -> str:
        return self.pretty()
