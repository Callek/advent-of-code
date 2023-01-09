"""2015 - Day 16"""
import os
import re
from pathlib import Path
from typing import Literal, TypedDict

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2015/days/16/input.txt")
)


# This typing is ugly, but it allows us to have cheap code in the filter
MFCSAM_RESULTS: dict[
    Literal["children"]
    | Literal["cats"]
    | Literal["samoyeds"]
    | Literal["pomeranians"]
    | Literal["akitas"]
    | Literal["vizslas"]
    | Literal["goldfish"]
    | Literal["trees"]
    | Literal["cars"]
    | Literal["perfumes"],
    int,
] = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

SUE_RE = re.compile(
    r"^Sue (?P<id>\d+)\: (?:(?:"
    r"(?:children: (?P<children>\d+))|"
    r"(?:cats: (?P<cats>\d+))|"
    r"(?:samoyeds: (?P<samoyeds>\d+))|"
    r"(?:pomeranians: (?P<pomeranians>\d+))|"
    r"(?:akitas: (?P<akitas>\d+))|"
    r"(?:vizslas: (?P<vizslas>\d+))|"
    r"(?:goldfish: (?P<goldfish>\d+))|"
    r"(?:trees: (?P<trees>\d+))|"
    r"(?:cars: (?P<cars>\d+))|"
    r"(?:perfumes: (?P<perfumes>\d+))"
    r"),? ?)*"
    r"$"
)


class Aunt(TypedDict):
    """A descriptor of an Aunt"""

    # pylint: disable=too-few-public-methods

    id: str

    children: str | None
    cats: str | None
    samoyeds: str | None
    pomeranians: str | None
    akitas: str | None
    vizslas: str | None
    goldfish: str | None
    trees: str | None
    cars: str | None
    perfumes: str | None


def parse_aunt(raw_text: str) -> list[Aunt]:
    """Parse out the aunt info"""
    aunts = []
    for line in raw_text.splitlines():
        match = SUE_RE.match(line)
        if not match:
            raise Exception(f"Huh {line}")
        matches = match.groupdict()
        aunts.append(
            Aunt(
                id=matches["id"],
                children=matches["children"],
                cats=matches["cats"],
                samoyeds=matches["samoyeds"],
                pomeranians=matches["pomeranians"],
                akitas=matches["akitas"],
                vizslas=matches["vizslas"],
                goldfish=matches["goldfish"],
                trees=matches["trees"],
                cars=matches["cars"],
                perfumes=matches["perfumes"],
            )
        )
    return aunts


def filter_for_part1(aunt: Aunt) -> bool:
    """Filter function for part 1, all keys == their value"""
    keep = True
    for mfcsam_key, mfcsam_result in MFCSAM_RESULTS.items():
        aunt_result: str | None = aunt[mfcsam_key]
        if aunt_result is None:
            continue
        if not mfcsam_result == int(aunt_result):
            keep = False
            break
    return keep


def part1(aunts: list[Aunt]) -> str:
    """Part 1"""
    aunt = list(filter(filter_for_part1, aunts))[0]
    return aunt["id"]


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text().strip()
    aunts = parse_aunt(raw_data)
    print(f"{__doc__} - Part 1: {part1(aunts)}")
    # print(f"{__doc__} - Part 2: {part2(ingredients)}")
