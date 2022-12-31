"""2015 - Day 9"""
import os
import sys
from dataclasses import dataclass, field
from itertools import permutations
from pathlib import Path

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2015/days/9/input.txt")
)


@dataclass
class CITY:
    """An arbitrary city"""

    name: str
    distances: dict[str, int] = field(default_factory=dict)

    def __eq__(self, other: object):
        if not isinstance(other, CITY):
            return False
        return self.name == other.name


def parse_list_of_string(data: str) -> list[str]:
    """Parsing Logic"""
    return data.strip().splitlines()


def get_cities(data: list[str]) -> dict[str, CITY]:
    """Get a list of cities"""
    cities: dict[str, CITY] = {}
    for line in data:
        (city1, _, city2, _, distance) = line.split(" ")
        cities.setdefault(city1, CITY(name=city1))
        cities.setdefault(city2, CITY(name=city2))

        cities[city1].distances[city2] = int(distance)
        cities[city2].distances[city1] = int(distance)
    return cities


def part1(cities: dict[str, CITY]) -> int:
    """Part 1"""
    min_distance = sys.maxsize
    for city_order in permutations(cities.values()):
        # Distance of this full permutation
        # city_order[:-1] -- the list without the last item (first arg)
        # city_order[1:] -- the list without the first item (second arg)
        # map/lambda - return distance along each hop
        dist = sum(
            map(
                lambda city, next_city: city.distances[next_city.name],
                city_order[:-1],
                city_order[1:],
            )
        )
        min_distance = min(min_distance, dist)
    return min_distance


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text()
    data = parse_list_of_string(raw_data)
    cities = get_cities(data)
    print(f"{__doc__} - Part 1: {part1(cities)}")
    # print(f"{__doc__} - Part 2: {part2(data)}")
