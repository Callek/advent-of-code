"""2015 - Day 4"""
import os
import hashlib
from itertools import count
from pathlib import Path

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2015/days/4/input.txt")
)


def parse_to_string(data: str) -> str:
    """Parsing Logic"""
    return data.strip()


def check_hash(hashed: str, zeroes: int = 5) -> bool:
    """Check the hash, retrun true if its good"""
    if hashed.startswith("000000"[:zeroes]):
        return True
    return False


def find_hash(salt: str, zeroes: int = 5) -> int:
    """Find a hash with X leading zeros"""
    hashed = hashlib.md5(salt.encode("utf-8"), usedforsecurity=False).hexdigest()
    if check_hash(hashed):
        raise Exception("Unexpected hash with no integer")
    for number in count():
        # Loop Infinitely
        hashed = hashlib.md5(
            f"{salt}{number}".encode("utf-8"), usedforsecurity=False
        ).hexdigest()
        if check_hash(hashed, zeroes):
            # We have 5 leading 0's
            return number
        if number > 100000000000000000000:
            break
    raise Exception("How did we get here")


def part1(salt: str) -> int:
    """Part 1

    Find a hash with 5 leading zeros
    """
    return find_hash(salt, zeroes=5)


def part2(salt: str) -> int:
    """Part 2

    Find a hash with 6 leading zeros
    """
    return find_hash(salt, zeroes=6)


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text()
    data = parse_to_string(raw_data)
    print(f"{__doc__} - Part 1: {part1(data)}")
    print(f"{__doc__} - Part 2: {part2(data)}")
