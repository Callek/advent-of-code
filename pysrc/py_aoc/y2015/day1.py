"""2015 - Day 1"""
import os
from pathlib import Path

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2015/days/1/input.txt")
)


def parse_to_string(data: str) -> str:
    """Parsing Logic"""
    return data.strip()


def part1(instructions: str) -> int:
    """Part 1

    Calculate Santa's Floor from instructions

    ( => Up
    ) => Down

    Matching is not required
    """
    start = 0
    up_instructions = instructions.count("(")
    down_instructions = instructions.count(")")
    return start + up_instructions - down_instructions


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text()
    data = parse_to_string(raw_data)
    print(f"{__doc__} - Part 1: {part1(data)}")
    # print(f"{__doc__} - Part 2: {part2(data)}")
