"""2022 - Day 5"""
import os
import re
from pathlib import Path

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2022/days/5/input.txt")
)


def parse_stack_start(stack_data: str) -> list[str]:
    """Parse Stack Data

    Returned as a list of strings, with *top* crate being first in the string
    """
    start_regex = re.compile(r"[\[ ]([ A-Z])[\] ](?: |$)")
    crates_start: list[str] = []
    for line in stack_data.splitlines():
        line_crates = start_regex.findall(line)
        for i, crate in enumerate(line_crates):
            while len(crates_start) <= i:
                crates_start.insert(i, "")
            crates_start[i] += crate.strip()
    return crates_start


def parse_directions(direction_data: str) -> list[tuple[int, ...]]:
    """Parse direction data"""

    # move 1 from 2 to 1
    direction_re = re.compile(r"move (\d*) from (\d*) to (\d*)")
    directions: list[tuple[int, ...]] = []
    for line in direction_data.splitlines():
        matched = direction_re.fullmatch(line)
        if not matched:
            raise Exception("Unexpected direction line format")
        directions.append(tuple(map(int, matched.groups())))
    return directions


def parse_data(data: str) -> tuple[list[str], list[tuple[int, ...]]]:
    """Parse out the starting crates, and the directions"""
    stuff = data.split("\n\n")
    assert len(stuff) == 2

    crates_start = parse_stack_start(stuff[0])
    directions = parse_directions(stuff[1])
    return crates_start, directions


def move_crates(
    orig_stack: list[str], directions: list[tuple[int, ...]], many: bool = False
) -> list[str]:
    """Move crates

    move X from Y to Z
    use the `many` boolean to indicate the crates move one at a time or many at once.

    Note: This function does not mutate `orig_stack`
    """
    stack = orig_stack[:]
    for direction in directions:
        move_num = direction[0]
        move_from = direction[1] - 1  # stacks are 0 indexed
        move_to = direction[2] - 1  # stacks are 0 indexed
        stack_moving = stack[move_from][:move_num]
        stack[move_from] = stack[move_from][move_num:]
        if many:
            # Prepend to stack since these are newest
            stack[move_to] = stack_moving + stack[move_to]
        else:
            # ..., and reverse since we move one at a time.
            stack[move_to] = stack_moving[::-1] + stack[move_to]
    return stack


def part1(start: list[str], directions: list[tuple[int, ...]]) -> str:
    """Part 1

    move X from Y to Z - one at a time.
    """
    stack = move_crates(start, directions)
    answer = "".join([s[0] for s in stack])
    return answer


def part2(start: list[str], directions: list[tuple[int, ...]]) -> str:
    """Part 2

    move X from Y to Z - many at a time.
    """
    stack = move_crates(start, directions, many=True)
    answer = "".join([s[0] for s in stack])
    return answer


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text()
    start, directions = parse_data(raw_data)
    print(f"{__doc__} - Part 1: {part1(start, directions)}")
    print(f"{__doc__} - Part 2: {part2(start, directions)}")
