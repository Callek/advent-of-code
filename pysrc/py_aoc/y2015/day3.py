"""2015 - Day 3"""
import os
from pathlib import Path

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2015/days/3/input.txt")
)


def parse_to_string(data: str) -> str:
    """Parsing Logic"""
    return data.strip()


def part1(instructions: str) -> int:
    """Part 1

    Follow the directions and count every house visited
    """
    pos_x = 0
    pos_y = 0
    houses: set[tuple[int, int]] = set()
    houses.add((pos_x, pos_y))
    for char in instructions:
        match char:
            case "^":
                pos_y += 1
            case "v":
                pos_y -= 1
            case ">":
                pos_x += 1
            case "<":
                pos_x -= 1
            case _:
                raise Exception(f"Unexpected Instruction '{char}'")
        houses.add((pos_x, pos_y))
    return len(houses)


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text()
    data = parse_to_string(raw_data)
    print(f"{__doc__} - Part 1: {part1(data)}")
    # print(f"{__doc__} - Part 2: {part2(data)}")
