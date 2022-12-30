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

    function: Callable[[bool], bool]
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


def toggle(light: bool) -> bool:
    """Perform a toggle"""
    return not light


def turn_on(light: bool) -> bool:
    """Turn on this light"""
    assert light is not None
    return True


def turn_off(light: bool) -> bool:
    """Turn off this light"""
    assert light is not None
    return False


def part1(commands: list[COMMAND]) -> int:
    """Part 1"""
    # pylint: disable=invalid-name
    grid: dict[tuple[int, int], bool] = {}
    for command in commands:
        for x in range(command.start.x, command.end.x + 1):
            for y in range(command.start.y, command.end.y + 1):
                grid[(x, y)] = command.function(grid.get((x, y), False))
    return len([light for light in grid.values() if light])


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text()
    data = parse_list_of_string(raw_data)
    commands = parse_commands(data)
    print(f"{__doc__} - Part 1: {part1(commands)}")
    # print(f"{__doc__} - Part 2: {part2(strings)}")
