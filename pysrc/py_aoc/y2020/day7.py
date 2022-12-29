"""2020 - Day 7"""
# pylint: disable=broad-except

import os
import re
from typing import Dict, List, Union, cast

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2020/days/7/input.txt")
)

BagListType = Dict[str, List[Dict[str, Union[int, str]]]]


def main() -> None:
    """Main Logic"""
    with open(inputfile) as infile:
        raw_data = infile.read()

    bags = parse_bags(raw_data.splitlines())
    gold_count = bags_containing_at_least_one_shiny_gold_bag(bags)
    print(f"Gold Count: {gold_count}")

    part2 = bag_count(bags, "shiny gold")
    print(f"Part 2 count: {part2}")


def parse_bags(lines: List[str]) -> BagListType:
    """Parse Bags from input"""
    bags: BagListType = {}
    outer_bag_re = re.compile(r"^(\w+ \w+) bags contain (.*)")
    contents_bag_re = re.compile(r"([0-9]+ )*(\w+ \w+) bag(?:s)?")

    for line in lines:
        matches = outer_bag_re.search(line)
        assert matches
        bag_type = matches.group(1)
        content_string = matches.group(2)[:-1]

        content_tuples = contents_bag_re.findall(content_string)

        bag_contents = []
        for content_tuple in content_tuples:
            if content_tuple[1] == "no other":
                continue
            bag_contents.append(
                {"count": int(content_tuple[0]), "type": content_tuple[1]}
            )

        bags[bag_type] = bag_contents
    return bags


def shiny_gold_bag_count(bag_collection: BagListType, bag_name: str) -> int:
    """Count shiny gold bags"""
    count = 0
    bag = bag_collection[bag_name]

    if len(bag) == 0:
        return count

    for sub_bag in bag:
        if sub_bag["type"] == "shiny gold":
            count += 1
        count += shiny_gold_bag_count(bag_collection, cast(str, sub_bag["type"]))

    return count


def bags_containing_at_least_one_shiny_gold_bag(bag_collection: BagListType) -> int:
    """Find count of bags with shiny gold bags"""
    count = 0

    for bag_name in bag_collection.keys():
        if shiny_gold_bag_count(bag_collection, bag_name) > 0:
            print(f"{bag_name} bags contain at least one shiny gold bag!")
            count += 1

    return count


def bag_count(bag_collection: BagListType, bag_name: str) -> int:
    """Count bags of bag_name"""
    count = 0
    top_level_bag = bag_collection[bag_name]
    print(f"Currently counting bags inside {bag_name}.")

    if len(top_level_bag) == 0:
        return count

    for current_bag in top_level_bag:
        print(
            f"There are {current_bag['count']} of {current_bag['type']} inside {bag_name}."
        )
        # Add the number of bags of the current type
        # to the count.
        current_bag_type_count = cast(int, current_bag["count"])
        count += current_bag_type_count
        # Count the bags inside each bag of the current type,
        # multiply it by the number of the current type,
        # then add it to the count.
        bags_inside_current_bag_type_count = bag_count(
            bag_collection, cast(str, current_bag["type"])
        )
        count += bags_inside_current_bag_type_count * current_bag_type_count

    return count
