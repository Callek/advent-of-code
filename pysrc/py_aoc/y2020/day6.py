"""2020 - Day 6"""
# pylint: disable=broad-except

import os
from typing import List

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2020/days/6/input.txt")
)


def main() -> None:
    """Main Logic"""
    with open(inputfile) as infile:
        raw_data = infile.read()

    sets = create_sets(raw_data)
    total = sum_yes_answers(sets)
    print(f"Total (answer for part 1): {total}")

    sets = create_sets_all_yes(raw_data)
    total = sum_yes_answers(sets)
    print(f"Total (answer for part 2): {total}")


def create_sets(raw_data: str) -> list[set[str]]:
    """Sets from data"""
    groups = []
    for group in raw_data.split("\n\n"):
        answers: set[str] = set()
        for person in group.split("\n"):
            answers |= set(person)
        groups.append(answers)
    return groups


def create_sets_all_yes(raw_data: str) -> list[set[str]]:
    """Sets with all yes"""
    groups: list[set[str]] = []
    for group in raw_data.split("\n\n"):
        answers: set[str] | None = None
        for person in group.split("\n"):
            if not person:
                continue
            if answers is None:
                answers = set(person)
            else:
                answers &= set(person)
        if answers:
            groups.append(answers)
    return groups


def sum_yes_answers(sets: List[set]) -> int:
    """Number of yes answers"""
    return sum(len(x) for x in sets)
