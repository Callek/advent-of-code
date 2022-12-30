"""2015 - Day 6"""
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2015/days/6/input.txt")
)


@dataclass
class COORD:
    """Coordiante"""

    # pylint: disable=invalid-name

    x: int
    y: int


@dataclass
class COMMAND:
    """Command"""

    function: Callable[[int, bool], int]
    start: COORD
    end: COORD


def parse_list_of_string(data: str) -> list[str]:
    """Parsing Logic"""
    return data.strip().splitlines()


def parse_commands(data: list[str]) -> list[COMMAND]:
    """Parse the data to commands"""
    # pylint: disable=invalid-name
    start_end_re = re.compile(r"(\d+),(\d+) through (\d+),(\d+)")
    commands: list[COMMAND] = []
    for line in data:
        if line.startswith("toggle"):
            func = toggle
        elif line.startswith("turn on"):
            func = turn_on
        elif line.startswith("turn off"):
            func = turn_off
        match = start_end_re.search(line)
        if not match:
            raise Exception(f"Unexpected Format '{line}'")
        x1, y1, x2, y2 = match.groups()
        commands.append(COMMAND(func, COORD(int(x1), int(y1)), COORD(int(x2), int(y2))))
    return commands


def toggle(light: int, second_part: bool = False) -> int:
    """Perform a toggle"""
    if second_part:
        return light + 2
    return int(not light > 0)


def turn_on(light: int, second_part: bool = False) -> int:
    """Turn on this light"""
    if second_part:
        return light + 1
    return 1


def turn_off(light: int, second_part: bool = False) -> int:
    """Turn off this light"""
    if second_part:
        if light > 0:
            return light - 1
        # intentional fall through to a floor of zero
    return 0


def part1(commands: list[COMMAND]) -> int:
    """Part 1"""
    # pylint: disable=invalid-name
    grid: dict[tuple[int, int], int] = {}
    for command in commands:
        for x in range(command.start.x, command.end.x + 1):
            for y in range(command.start.y, command.end.y + 1):
                grid[(x, y)] = command.function(grid.get((x, y), 0), False)
    return len([light for light in grid.values() if light > 0])


def part2(commands: list[COMMAND]) -> int:
    """Part 2"""
    # pylint: disable=invalid-name
    grid: dict[tuple[int, int], int] = {}
    for command in commands:
        for x in range(command.start.x, command.end.x + 1):
            for y in range(command.start.y, command.end.y + 1):
                grid[(x, y)] = command.function(grid.get((x, y), 0), True)
    return sum(light for light in grid.values())


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text()
    data = parse_list_of_string(raw_data)
    commands = parse_commands(data)
    print(f"{__doc__} - Part 1: {part1(commands)}")
    print(f"{__doc__} - Part 2: {part2(commands)}")
