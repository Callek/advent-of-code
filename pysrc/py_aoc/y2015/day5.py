"""2015 - Day 5"""
import os
import re
from pathlib import Path

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2015/days/5/input.txt")
)

THREE_VOWEL_REGEX = re.compile(r"(?:[aeiou].*){3}")
TWO_LETTER_REGEX = re.compile(r"(.)\1")


def parse_list_of_string(data: str) -> list[str]:
    """Parsing Logic"""
    return data.strip().splitlines()


def has_three_vowels(string: str) -> bool:
    """Check if this contains at least 3 vowels"""
    return bool(THREE_VOWEL_REGEX.search(string))


def has_double_letter(string: str) -> bool:
    """Check if the string has at least one double letter"""
    return bool(TWO_LETTER_REGEX.search(string))


def no_naughty_string(string: str) -> bool:
    """Check if any of the naughty list is in the string"""
    naughty_list = ["ab", "cd", "pq", "xy"]
    return not any(naughty in string for naughty in naughty_list)


def part1(strings: list[str]) -> int:
    """Part 1

    Find a hash with 5 leading zeros
    """
    count = 0
    for string in strings:
        if all(
            (
                has_three_vowels(string),
                has_double_letter(string),
                no_naughty_string(string),
            )
        ):
            count += 1
    return count


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text()
    strings = parse_list_of_string(raw_data)
    print(f"{__doc__} - Part 1: {part1(strings)}")
    # print(f"{__doc__} - Part 2: {part2(data)}")
