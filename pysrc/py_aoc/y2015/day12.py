"""2015 - Day 12"""
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


def count_numbers(json_obj: JSON_OBJECT_NESTING_TYPES, ignore_red=False) -> int:
    """Recursively count numbers in json_obj"""
    if isinstance(json_obj, int):
        return json_obj
    if isinstance(json_obj, str):
        return 0
    if isinstance(json_obj, list):
        return sum(count_numbers(val, ignore_red=ignore_red) for val in json_obj)
    assert isinstance(json_obj, dict)
    if ignore_red and "red" in json_obj.values():
        return 0
    return sum(count_numbers(val, ignore_red=ignore_red) for val in json_obj.values())


def part1(blob: str) -> int:
    """Part 1"""
    json_object: JSON_OBJECT_NESTING_TYPES = json.loads(blob)
    return count_numbers(json_object)


def part2(blob: str) -> int:
    """Part 2"""
    json_object: JSON_OBJECT_NESTING_TYPES = json.loads(blob)
    return count_numbers(json_object, ignore_red=True)


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text().strip()
    print(f"{__doc__} - Part 1: {part1(raw_data)}")
    print(f"{__doc__} - Part 2: {part2(raw_data)}")
