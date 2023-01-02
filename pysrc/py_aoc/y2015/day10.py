"""2015 - Day 10"""
import os
from itertools import groupby
from pathlib import Path

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2015/days/10/input.txt")
)


def step_look_and_say(num: str) -> str:
    """Do a single step of look and say"""
    new_num = ""
    for group, value in groupby(num):
        new_num += f"{len(list(value))}{group}"
    return new_num


def do_look_and_say(num: str, iterations=5) -> str:
    """Do a specific number of iterations of look and say"""
    new_num = num
    for _ in range(iterations):
        new_num = step_look_and_say(new_num)
    return new_num


def part1(num: str) -> int:
    """Part 1"""
    return len(do_look_and_say(num.strip(), iterations=40))


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text()
    print(f"{__doc__} - Part 1: {part1(raw_data)}")
    # print(f"{__doc__} - Part 2: {part2(cities)}")
