"""2022 - Day 4"""
import os
import re
from pathlib import Path
from typing import Callable

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2022/days/4/input.txt")
)


def parse_assignments(data: str) -> list[str]:
    """Parse out the list of rucksacks"""
    return data.strip().split("\n")


def any_overlap(elf_a_range: set[range], elf_b_range: set[range]) -> bool:
    """Test if any of the two ranges overlap"""
    if elf_a_range.issuperset(elf_b_range) or elf_a_range.issubset(elf_b_range):
        return True
    return False


def some_overlap(elf_a_range: set[range], elf_b_range: set[range]) -> bool:
    """Test if there is any overlap between the two ranges"""
    if elf_a_range.isdisjoint(elf_b_range):
        # No overlap
        return False
    return True


def check_elf_assignments(
    assignments: list[str], checker: Callable[[set[range], set[range]], bool]
) -> int:
    """Find count of assignments that match a given check

    - Split the assignments by elf A and elf B
    - Generate a range of int's converted to set
    - Run through checker function to see if we should count the assignment
    - return ranges where checker was true

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
        if checker(elf_a_range, elf_b_range):
            overlapped += 1

    return overlapped


def part1(assignments: list[str]) -> int:
    """Part 1

    number of times an elf in an assigment is fully duplicating work.
    """
    return check_elf_assignments(
        assignments,
        any_overlap,
    )


def part2(assignments: list[str]) -> int:
    """Part 2

    number of times an elf in an assigment has any duplicating work.
    """
    return check_elf_assignments(
        assignments,
        some_overlap,
    )


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text()
    assignments = parse_assignments(raw_data)
    print(f"{__doc__} - Part 1: {part1(assignments)}")
    print(f"{__doc__} - Part 2: {part2(assignments)}")
