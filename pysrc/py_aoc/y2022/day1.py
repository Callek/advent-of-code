"""2022 - Day 1"""
import os
from pathlib import Path

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2022/days/1/input.txt")
)


def parse_to_list_of_list_of_ints(data: str) -> list[list[int]]:
    """Parsing Logic"""
    return [
        [int(food) for food in elf.split("\n")] for elf in data.strip().split("\n\n")
    ]


def part1(data: list[list[int]]) -> int:
    """Part 1

    Sum all elfs food and return that total
    """
    return max(sum(elf) for elf in data)


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text()
    data = parse_to_list_of_list_of_ints(raw_data)
    print(f"{__doc__} - Part 1: {part1(data)}")
