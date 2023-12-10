"""2015 - Day 11"""
import os
import re
from pathlib import Path

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2015/days/11/input.txt")
)


DOUBLES_RE = re.compile(r"([a-z])\1.*([a-z])\2")


def next_password(password: str) -> str:
    """Find the next potential password given the previous"""
    force_turn_over = False
    chars = [ord(letter) for letter in password]
    ambiguous_chars = (ord("i"), ord("l"), ord("o"))
    for char in range(len(password)):
        if force_turn_over:
            chars[char] = ord("z")
        if chars[char] in ambiguous_chars:
            force_turn_over = True
    for char in range(len(password) - 1, -1, -1):
        if chars[char] == ord("z"):
            chars[char] = ord("a")
        else:
            chars[char] += 1
            break
    return "".join(chr(char) for char in chars)


def validate_bad_letters(password: str) -> bool:
    """Validate the non-existance of letters"""
    return set("iol").isdisjoint(set(password))


def validate_doubles(password: str) -> bool:
    """Validate that there are two sets of different doubles"""
    ret = DOUBLES_RE.search(password)
    return bool(ret)


def validate_consecutive_string(password: str) -> bool:
    """Validate a consecutive string exists"""
    validated = False
    for idx in range(len(password) - 2):
        start = ord(password[idx])
        if ord(password[idx + 1]) == start + 1 and ord(password[idx + 2]) == start + 2:
            validated = True
            break
    return validated


def check_password(password: str) -> bool:
    """Check if the current password is valid"""
    return (
        validate_bad_letters(password)
        and validate_doubles(password)
        and validate_consecutive_string(password)
    )


def part1(password: str) -> str:
    """Part 1"""
    password_part1 = password
    while not check_password(password_part1):
        password_part1 = next_password(password_part1)
    return password_part1


def part2(password: str) -> str:
    """Part 1"""
    password_part2 = next_password(password)
    while not check_password(password_part2):
        password_part2 = next_password(password_part2)
    return password_part2


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text().strip()
    part1_pw = part1(raw_data)
    print(f"{__doc__} - Part 1: {part1_pw}")
    print(f"{__doc__} - Part 2: {part2(part1_pw)}")
