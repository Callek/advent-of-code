"""2015 - Day 13"""
import os
import re
from dataclasses import dataclass, field
from itertools import permutations
from pathlib import Path


inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2015/days/13/input.txt")
)

PERSON_PREFERENCES_RE = re.compile(
    r"^(?P<who>[a-zA-Z]+) would (?P<gain>gain|lose) (?P<amount>\d+) happiness "
    r"units by sitting next to (?P<who2>[a-zA-Z]+)\.$"
)


@dataclass
class Person:
    """A descriptor of a person"""

    desires: dict[str, int] = field(default_factory=dict)

    def happiness(self, person_1, person_2) -> int:
        """How happy we are with a given seat placement"""
        return self.desires[person_1] + self.desires[person_2]


def parse_people(raw_text: str) -> dict[str, Person]:
    """Parse out the people"""
    preferences: dict[str, Person] = {}
    for line in raw_text.splitlines():
        match = PERSON_PREFERENCES_RE.match(line)
        if not match:
            raise Exception(f"Huh {line}")
        who, gain, amount, who2 = match.groups()
        assert all([who, gain, amount, who2])
        neg = -1 if gain == "lose" else 1
        happiness_change = neg * int(amount)
        person = preferences.get(who, Person())
        person.desires[who2] = happiness_change
        preferences[who] = person
    return preferences


def happy_for_ordered(people_order: tuple[str, ...], people: dict[str, Person]) -> int:
    """Get the happiness of a given order"""
    happy = 0
    for idx, name in enumerate(people_order):
        person = people[name]
        # idx - 1 ==  automatically rotates around the length
        happy += person.desires[people_order[idx - 1]]
        # (len(people_order) - 1) == magic to get 'next' entry even if we're
        # at the end of the tuple
        happy += person.desires[people_order[idx - (len(people_order) - 1)]]
    return happy


def part1(people: dict[str, Person]) -> int:
    """Part 1"""
    max_happy = 0
    for order in permutations(people.keys()):
        curr_happy = happy_for_ordered(order, people)
        max_happy = max(max_happy, curr_happy)
    return max_happy


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text().strip()
    people = parse_people(raw_data)
    print(f"{__doc__} - Part 1: {part1(people)}")
    # print(f"{__doc__} - Part 2: {part2(raw_data)}")
