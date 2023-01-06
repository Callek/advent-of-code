"""2015 - Day 13"""
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Literal


inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2015/days/14/input.txt")
)


REINDEER_RE = re.compile(
    r"^(?P<name>[a-zA-Z]+) can fly (?P<speed>\d+) km/s for (?P<stamina>\d+) "
    r"seconds, but then must rest for (?P<rest>\d+) seconds\.$"
)


@dataclass
class Reindeer:
    """A descriptor of a Raindeer"""

    name: str

    # Start flying
    state: Literal["flying"] | Literal["resting"]
    # Duration we've been in this state
    seconds_in_state: int

    # km/s
    speed: int
    # Length of time able to keep speed
    stamina: int
    # Rest time needed to recover
    rest: int

    total_distance: int = 0

    def advance(self, seconds: int = 1) -> None:
        """Advanced this reindeer"""
        seconds_elapsed: int = 0
        while seconds > seconds_elapsed:
            available_seconds = seconds - seconds_elapsed
            match self.state:
                case "resting":
                    remaining_rest_time = self.rest - self.seconds_in_state
                    if available_seconds > remaining_rest_time:
                        seconds_elapsed += remaining_rest_time
                        self.seconds_in_state = 0
                        self.state = "flying"
                        continue
                    self.seconds_in_state += available_seconds
                    seconds_elapsed += available_seconds
                    continue
                case "flying":
                    remaining_flying_time = self.stamina - self.seconds_in_state
                    if available_seconds > remaining_flying_time:
                        seconds_elapsed += remaining_flying_time
                        self.seconds_in_state = 0
                        self.state = "resting"
                        self.total_distance += remaining_flying_time * self.speed
                        continue
                    self.seconds_in_state += available_seconds
                    seconds_elapsed += available_seconds
                    self.total_distance += available_seconds * self.speed
                    continue


def parse_reindeer(raw_text: str) -> list[Reindeer]:
    """Parse out the people"""
    deer = []
    for line in raw_text.splitlines():
        match = REINDEER_RE.match(line)
        if not match:
            raise Exception(f"Huh {line}")
        name, speed, stamina, rest = match.groups()
        assert all([name, speed, stamina, rest])
        deer.append(
            Reindeer(
                name=name,
                state="flying",
                seconds_in_state=0,
                speed=int(speed),
                stamina=int(stamina),
                rest=int(rest),
            )
        )
    return deer


def advance_all_reindeer(deers: list[Reindeer], seconds=1) -> None:
    """Advances the reindeer X seconds"""
    for deer in deers:
        deer.advance(seconds)


def part1(deers: list[Reindeer], seconds: int = 2503) -> int:
    """Part 1"""
    advance_all_reindeer(deers, seconds)
    return max(deer.total_distance for deer in deers)


def main() -> None:
    """Main Logic"""

    raw_data = Path(inputfile).read_text().strip()
    deer = parse_reindeer(raw_data)
    print(f"{__doc__} - Part 1: {part1(deer)}")
    # print(f"{__doc__} - Part 2: {part2(people)}")
