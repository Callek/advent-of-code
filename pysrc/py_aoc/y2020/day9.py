"""2020 - Day 9"""
# pylint: disable=broad-except

import os
from collections import deque
from functools import reduce
from itertools import permutations

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2020/days/9/input.txt")
)


def main() -> None:
    """Main Logic"""
    with open(inputfile) as infile:
        raw_data = infile.read()

    part1_val = part1(raw_data)
    print(f"Answer for part1 is {part1_val}")
    part2_val = part2(raw_data, part1_val)
    print(f"Answer for part2 is {part2_val}")


def part1(data: str, preamble: int = 25) -> int:
    """Part 1"""
    nums = data.splitlines()
    deck: deque = deque(maxlen=preamble)
    for num in nums:
        if len(deck) < preamble:
            deck.append(int(num))
            continue
        valid = map(lambda a: a[0] + a[1], permutations(deck, r=2))
        if int(num) in valid:
            deck.append(int(num))
        else:
            return int(num)
    return 0


def part2(data: str, target: int) -> int:
    """Part 2"""
    nums = list(map(int, data.splitlines()))
    for idx in range(len(nums)):
        value = part2_inner(nums, idx, target)
        if value == -1:
            continue

        return value
    raise Exception("Unexpectedly found no result")


def part2_inner(nums, idx, target) -> int:
    """Inner for loop for part 2"""
    for end in range(idx + 1, len(nums)):
        added = reduce(lambda a, b: a + b, nums[idx : end + 1])
        if added > int(target):
            return -1
        if added != int(target):
            continue
        return min(nums[idx : end + 1]) + max(nums[idx : end + 1])
    return -1
