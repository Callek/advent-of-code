"""2015 - Day 3"""
import os
from pathlib import Path

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2015/days/3/input.txt")
)


def parse_to_string(data: str) -> str:
    """Parsing Logic"""
    return data.strip()


def move(position: tuple[int, int], direction: str) -> tuple[int, int]:
    """Given a starting position and direction string move one space

    Returns the new position
    """
    pos_x, pos_y = position
    match direction:
        case "^":
            pos_y += 1
        case "v":
            pos_y -= 1
        case ">":
            pos_x += 1
        case "<":
            pos_x -= 1
        case _:
            raise Exception(f"Unexpected Instruction '{direction}'")
    return (pos_x, pos_y)


def part1(instructions: str) -> int:
    """Part 1

    Follow the directions and count every house visited
    """
    santa = (0, 0)
    houses: set[tuple[int, int]] = set()
    houses.add(santa)
    for char in instructions:
        santa = move(santa, char)
        houses.add(santa)
    return len(houses)


def part2(instructions: str) -> int:
    """Part 2

    Follow the directions and count every house visited
    Santa moves every even-index
    Robo Santa moves every odd index
    """
    santa = (0, 0)
    robo = (0, 0)
    houses: set[tuple[int, int]] = set()
    houses.add(santa)
    houses.add(robo)
    for idx in range(0, len(instructions), 2):
        santa_dir = instructions[idx]
        robo_dir = instructions[idx + 1]
        santa = move(santa, santa_dir)
        robo = move(robo, robo_dir)
        houses.add(santa)
        houses.add(robo)
    return len(houses)


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text()
    data = parse_to_string(raw_data)
    print(f"{__doc__} - Part 1: {part1(data)}")
    print(f"{__doc__} - Part 2: {part2(data)}")
