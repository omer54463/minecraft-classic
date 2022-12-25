from argparse import ArgumentParser, Namespace
from pathlib import Path
from minecraft_classic.message_packet import MessagePacket
from minecraft_classic.packet import Packet
from minecraft_classic.parse import parse
from minecraft_classic.set_block_client_packet import SetBlockClientPacket
import matplotlib.pyplot as plt  # type: ignore


def parse_arguments() -> Namespace:
    argument_parser = ArgumentParser()
    argument_parser.add_argument(
        "file_path", help="Path to a file containing the stream data."
    )
    return argument_parser.parse_args()


def read_packets(file_path: Path) -> list[Packet]:
    return [packet for _, packet in parse(file_path.read_bytes())]


def get_chat(packets: list[Packet]) -> list[str]:
    return [
        packet.text.decode().strip()
        for packet in packets
        if isinstance(packet, MessagePacket)
    ]


def get_blocks(packets: list[Packet]) -> list[tuple[int, int, int]]:
    points: list[tuple[int, int, int]] = []

    for packet in packets:
        if not isinstance(packet, SetBlockClientPacket):
            continue

        point = (packet.x, packet.y, packet.z)
        if packet.place:
            points.append(point)

        else:
            points.remove(point)

    return points


def main() -> None:
    arguments = parse_arguments()

    file_path = Path(arguments.file_path)
    packets = read_packets(file_path)
    chat = get_chat(packets)
    blocks = get_blocks(packets)

    for line in chat:
        print(line)

    xs = [x for x, _, _ in blocks]
    ys = [y for _, y, _ in blocks]

    plt.scatter(xs, ys)
    ca = plt.gca()
    ca.set_ylim([30, 60])
    plt.show()


if __name__ == "__main__":
    main()
