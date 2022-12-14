"""Tests for day 12"""
from py_aoc.y2021 import day12

from pytest import mark


EXAMPLE_DATA = [
    """start-A
start-b
A-c
A-b
b-d
A-end
b-end
""",
    """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""",
    """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""",
]


@mark.parametrize(
    "data,expect",
    (
        [EXAMPLE_DATA[0], 10],
        [EXAMPLE_DATA[1], 19],
        [EXAMPLE_DATA[2], 226],
    ),
)
def test_part1(data: str, expect: int) -> None:
    """Test part 1"""
    segments = day12.get_path_segments(data)
    assert day12.part1(segments) == expect


@mark.parametrize(
    "data,expect",
    (
        [EXAMPLE_DATA[0], 36],
        [EXAMPLE_DATA[1], 103],
        [EXAMPLE_DATA[2], 3509],
    ),
)
def test_part2(data: str, expect: int) -> None:
    """Test part 2"""
    segments = day12.get_path_segments(data)
    assert day12.part2(segments) == expect
