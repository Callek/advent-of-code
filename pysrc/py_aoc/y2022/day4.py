"""2022 - Day 4"""
import os
import re
from pathlib import Path

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2022/days/4/input.txt")
)


def parse_assignments(data: str) -> list[str]:
    """Parse out the list of rucksacks"""
    return data.strip().split("\n")


def part1(assignments: list[str]) -> int:
    """Part 1

    - Split the assignments by elf A and elf B
    - Generate a range of int's convert to set
    - identify if elf A is a superset
    - return ranges where there is a full overlap

    Note: max is inclusive
    """
    pattern = re.compile(r"(?P<a_min>\d*)-(?P<a_max>\d*),(?P<b_min>\d*)-(?P<b_max>\d*)")
    overlapped = 0
    for cleaning_pair in assignments:
        match = pattern.fullmatch(cleaning_pair)
        elf_a_range = set(
            range(int(match.group("a_min")), int(match.group("a_max")) + 1)
        )
        elf_b_range = set(
            range(int(match.group("b_min")), int(match.group("b_max")) + 1)
        )
        if elf_a_range.issuperset(elf_b_range) or elf_a_range.issubset(elf_b_range):
            overlapped += 1

    return overlapped


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text()
    assignments = parse_assignments(raw_data)
    print(f"{__doc__} - Part 1: {part1(assignments)}")
