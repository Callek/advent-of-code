"""2015 - Day 11"""
import os
import json
from pathlib import Path
from typing import TypeAlias

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2015/days/12/input.txt")
)


JSON_OBJECT_NESTING_TYPES: TypeAlias = (
    int
    | str
    | dict[str, "JSON_OBJECT_NESTING_TYPES"]
    | list["JSON_OBJECT_NESTING_TYPES"]
)


def count_numbers(json_obj: JSON_OBJECT_NESTING_TYPES) -> int:
    """Recursively count numbers in json_obj"""
    if isinstance(json_obj, int):
        return json_obj
    if isinstance(json_obj, str):
        return 0
    if isinstance(json_obj, list):
        return sum(count_numbers(val) for val in json_obj)
    assert isinstance(json_obj, dict)
    return sum(count_numbers(val) for val in json_obj.values())


def part1(blob: str) -> int:
    """Part 1"""
    json_object: JSON_OBJECT_NESTING_TYPES = json.loads(blob)
    return count_numbers(json_object)


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text().strip()
    print(f"{__doc__} - Part 1: {part1(raw_data)}")
    # print(f"{__doc__} - Part 2: {part2(part1_pw)}")
