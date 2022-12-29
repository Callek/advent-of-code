"""2015 - Day 2"""
import os
from dataclasses import dataclass
from pathlib import Path

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2015/days/2/input.txt")
)


@dataclass
class BOX:
    """A box
        +--------+
       /        /|
      /   2    / |
     /        /  |
    +--------+   | h
    |        | 3 |
    |        |   +
    |   1    |  /
    |        | /
    |        |/  l
    +--------+
        w

    Where w=width, h=height, l=length
    Numbers are Sides used in this days code.
    """

    # pylint: disable=invalid-name
    l: int
    w: int
    h: int


def parse_box_dimensions(data: str) -> list[BOX]:
    """Parses the box dimensions"""
    l_side: str
    w_side: str
    h_side: str
    return [
        BOX(int(l_side), int(w_side), int(h_side))
        for line in data.splitlines()
        for (l_side, w_side, h_side) in [(line.split("x", 2))]
    ]


def paper_for_present(box: BOX) -> int:
    """Paper needed for this present

    Surface Area + <smallest side area>
    """
    side_1 = box.w * box.h
    side_2 = box.w * box.l
    side_3 = box.h * box.l
    extra = min(side_1, side_2, side_3)
    return 2 * side_1 + 2 * side_2 + 2 * side_3 + extra


def part1(boxes: list[BOX]) -> int:
    """Part 1

    Identify total amount of wrapping paper needed.
    """
    return sum(paper_for_present(box) for box in boxes)


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text()
    boxes = parse_box_dimensions(raw_data)
    print(f"{__doc__} - Part 1: {part1(boxes)}")
    # print(f"{__doc__} - Part 2: {part2(data)}")
