from typing import Generator
from minecraft_classic.opcode import Opcode
from minecraft_classic.packet import Packet
from minecraft_classic.add_entity_packet import AddEntityPacket
from minecraft_classic.custom_block_level_packet import CustomBlockLevelPacket
from minecraft_classic.entity_teleport_packet import EntityTeleportPacket
from minecraft_classic.ext_info_packet import ExtInfoPacket
from minecraft_classic.level_begin_packet import LevelBeginPacket
from minecraft_classic.level_data_packet import LevelDataPacket
from minecraft_classic.login_packet import LoginPacket
from minecraft_classic.ext_entry_packet import ExtEntryPacket
from minecraft_classic.message_packet import MessagePacket
from minecraft_classic.set_block_client_packet import SetBlockClientPacket
from minecraft_classic.set_block_packet import SetBlockPacket
from minecraft_classic.level_end_packet import LevelEndPacket
from minecraft_classic.two_way_ping_packet import TwoWayPingPacket

OPCODE_PACKET_DICT: dict[Opcode, type[Packet]] = {
    Opcode.HANDSHAKE: LoginPacket,
    Opcode.EXT_INFO: ExtInfoPacket,
    Opcode.EXT_ENTRY: ExtEntryPacket,
    Opcode.CUSTOM_BLOCK_LEVEL: CustomBlockLevelPacket,
    Opcode.ENTITY_TELEPORT: EntityTeleportPacket,
    Opcode.TWO_WAY_PING: TwoWayPingPacket,
    Opcode.MESSAGE: MessagePacket,
    Opcode.SET_BLOCK_CLIENT: SetBlockClientPacket,
    Opcode.LEVEL_BEGIN: LevelBeginPacket,
    Opcode.LEVEL_DATA: LevelDataPacket,
    Opcode.LEVEL_END: LevelEndPacket,
    Opcode.ADD_ENTITY: AddEntityPacket,
    Opcode.SET_BLOCK: SetBlockPacket,
}


def parse_packet(data: bytes) -> tuple[Packet, bytes]:
    opcode = Opcode(data[0])

    if opcode not in OPCODE_PACKET_DICT:
        raise ValueError(f"Encountered unknown Opcode {opcode.name}")

    return OPCODE_PACKET_DICT[opcode].parse(data)


def parse(data: bytes) -> Generator[tuple[int, Packet], None, None]:
    total_length = len(data)
    while len(data) > 0:
        offset = total_length - len(data)
        packet, data = parse_packet(data)
        yield offset, packet
