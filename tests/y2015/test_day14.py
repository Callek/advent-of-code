"""2015 - Day 14"""
from py_aoc.y2015 import day14


TEST_DATA = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
"""


def test_part1() -> None:
    """Test Part 1"""

    deers = day14.parse_reindeer(TEST_DATA)
    assert 1120 == day14.part1(deers, seconds=1000)
