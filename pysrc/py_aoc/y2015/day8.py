"""2015 - Day 6"""
import os
import codecs
from pathlib import Path

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2015/days/8/input.txt")
)


def parse_list_of_string(data: str) -> list[str]:
    """Parsing Logic"""
    return data.strip().splitlines()


def parse_string(string: str) -> str:
    """Parse the string"""
    assert string.startswith('"') and string.endswith('"')
    inner_string = bytes(string[1:-1], encoding="utf-8")
    return codecs.getdecoder("unicode_escape")(inner_string)[0]


def re_encode_string(string: str) -> str:
    """Re-Encode the string"""
    encoded = string.encode("unicode_escape").decode("utf-8")
    escaped_quotes = encoded.replace('"', r"\"")
    return f'"{escaped_quotes}"'


def part1(data: list[str]) -> int:
    """Part 1"""
    code = 0
    memory = 0
    for line in data:
        code += len(line.strip())
        memory += len(parse_string(line.strip()))
    return code - memory


def part2(data: list[str]) -> int:
    """Part 1"""
    code = 0
    orig_code = 0
    for line in data:
        code += len(re_encode_string(line.strip()))
        orig_code += len(line.strip())
    return code - orig_code


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text()
    data = parse_list_of_string(raw_data)
    print(f"{__doc__} - Part 1: {part1(data)}")
    print(f"{__doc__} - Part 2: {part2(data)}")
