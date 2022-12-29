"""2020 - Day 7"""
from py_aoc.y2020 import day7

TEST_DATA1 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""


def test_day7() -> None:
    """Test Parsing"""
    parsed = day7.parse_bags(TEST_DATA1.splitlines())
    assert len(parsed) == 9
    assert parsed["faded blue"] == []
    assert len(parsed["muted yellow"]) == 2
    assert len(parsed["bright white"]) == 1
    assert parsed["muted yellow"][1]["count"] == 9
    assert parsed["muted yellow"][0]["count"] == 2
