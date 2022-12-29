"""2020 - Day 8"""
# pylint: disable=broad-except

import os
import copy
from typing import List, Tuple

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2020/days/8/input.txt")
)


def main() -> None:
    """Main Logic"""
    with open(inputfile) as infile:
        raw_data = infile.read()

    part1_val = part1(raw_data)
    print(f"Answer for part1 is {part1_val}")
    part2_val = part2(raw_data)
    print(f"Answer for part2 is {part2_val}")


def parse_instructions(data) -> List[Tuple[str, int]]:
    """Parse instructions"""
    # Assumes well formed
    instructions = []
    for line in data.splitlines():
        if not line:
            continue
        value, str_num = line.split()
        instructions.append((value, int(str_num)))
    return instructions


def part1(data) -> int:
    """Run the program and return once repeated"""
    instructions = parse_instructions(data)
    accumulator = 0
    idx = 0
    seen_indexes = set()
    while idx not in seen_indexes:
        seen_indexes.add(idx)
        if instructions[idx][0] == "nop":
            idx += 1
            continue
        if instructions[idx][0] == "jmp":
            idx += instructions[idx][1]
            continue
        if instructions[idx][0] == "acc":
            accumulator += instructions[idx][1]
            idx += 1
            continue

    return accumulator


def part2(data) -> int:
    """Part 2 - Find the modification to completely run the program"""
    instructions = parse_instructions(data)
    accumulator = 0
    for instruction_idx in range(len(instructions)):
        new_instructions = copy.deepcopy(instructions)
        if new_instructions[instruction_idx][0] == "acc":
            continue
        if new_instructions[instruction_idx][0] == "jmp":
            new_instructions[instruction_idx] = (
                "nop",
                new_instructions[instruction_idx][1],
            )
        elif new_instructions[instruction_idx][0] == "nop":
            new_instructions[instruction_idx] = (
                "jmp",
                new_instructions[instruction_idx][1],
            )

        accumulator = 0
        idx = 0
        seen_indexes = set()
        length = len(new_instructions)
        while idx not in seen_indexes:
            if idx >= length:
                return accumulator
            seen_indexes.add(idx)
            if new_instructions[idx][0] == "nop":
                idx += 1
                continue
            if new_instructions[idx][0] == "jmp":
                idx += new_instructions[idx][1]
                continue
            if new_instructions[idx][0] == "acc":
                accumulator += new_instructions[idx][1]
                idx += 1
                continue

    raise Exception("Unexpected Late Exit")
