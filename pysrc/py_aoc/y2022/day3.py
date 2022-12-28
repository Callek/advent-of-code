"""2022 - Day 3"""
import os
from pathlib import Path

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2022/days/3/input.txt")
)


def parse_rucksacks(data: str) -> list[str]:
    """Parse out the list of rucksacks"""
    return data.strip().split("\n")


def get_item_prio(item: str) -> int:
    """Return priority for a given item"""
    assert len(item) == 1
    if ord(item) > 96:
        # ord('a') == 97; ord('z') == 122
        # return a->z => 1->26
        return ord(item) - 96
    # must be 'A' -> 'Z'
    # ord('A') == 65; ord('Z') == 90
    # return A->Z => 27->52
    return ord(item) - 38


def rucksack_compartments(sack: str) -> list[str]:
    """Splits the rucksack contents into two compartments"""
    if len(sack) % 2:
        raise ValueError(
            f'Somehow this sack ("{sack}") does not have equal compartments'
        )
    # Due to even length, this will always work out.
    mid_idx = len(sack) // 2
    return [sack[:mid_idx], sack[mid_idx:]]


def part1(sacks: list[str]) -> int:
    """Solves for part 1

    - takes the sack
    - gets both compartments
    - finds item in both compartments
    - returns the priority
    """
    all_priorities_sum = 0
    for sack in sacks:
        compartment_a, compartment_b = rucksack_compartments(sack)
        dupelicate_item = set(compartment_a) & set(compartment_b)
        assert len(dupelicate_item) == 1
        all_priorities_sum += get_item_prio(dupelicate_item.pop())
    return all_priorities_sum


def part2(sacks: list[str]) -> int:
    """Solves for part 2

    - takes the sacks from elves in groups of 3
    - finds the common component
    - returns the priority of all components
    """
    all_priorities_sum = 0
    for i in range(0, len(sacks), 3):
        comp_a, comp_b, comp_c = sacks[i : i + 3]
        badge = set(comp_a) & set(comp_b) & set(comp_c)
        assert len(badge) == 1
        all_priorities_sum += get_item_prio(badge.pop())
    return all_priorities_sum


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text()
    sacks = parse_rucksacks(raw_data)
    print(f"{__doc__} - Part 1: {part1(sacks)}")
    print(f"{__doc__} - Part 2: {part2(sacks)}")
