"""2020 - Day 4"""
# pylint: disable=broad-except

import os
import re
from typing import Dict, List

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2020/days/4/input.txt")
)


def validate_birth_year(data: str) -> bool:
    """validate birth"""
    try:
        if 1920 <= int(data) <= 2002:
            return True
    except Exception:
        pass
    return False


def validate_issue_year(data: str) -> bool:
    """validate issue"""
    try:
        if 2010 <= int(data) <= 2020:
            return True
    except Exception:
        pass
    return False


def validate_exp_year(data: str) -> bool:
    """validate expiration"""
    try:
        if 2020 <= int(data) <= 2030:
            return True
    except Exception:
        pass
    return False


def validate_height(data: str) -> bool:
    """validate height"""
    if "cm" not in data and "in" not in data:
        return False
    match = re.match(r"(?P<height>\d+)(?P<units>(?:cm|in))$", data)
    assert match
    if match["units"] == "cm":
        if 150 <= int(match["height"]) <= 193:
            return True
    if match["units"] == "in":
        if 59 <= int(match["height"]) <= 76:
            return True
    return False


def validate_hair_color(data: str) -> bool:
    """validate hair color"""
    match = re.match(r"#[a-f0-9]{6}$", data)
    if match:
        return True
    return False


def validate_eye_color(data: str) -> bool:
    """validate eye color"""
    valid = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    if data in valid:
        return True
    return False


def validate_passport_id(data: str) -> bool:
    """validate passport id"""
    match = re.match(r"[0-9]{9}$", data)
    if match:
        return True
    return False


def validate_cid(_: str) -> bool:
    """Validate cid

    explicitly always valid"""
    return True


fields = {
    "byr": validate_birth_year,  # Birth Year
    "iyr": validate_issue_year,  # Issue Year
    "eyr": validate_exp_year,  # Expiration Year
    "hgt": validate_height,  # validate_height,  # Height
    "hcl": validate_hair_color,  # validate_hair_color,  # Hair Color
    "ecl": validate_eye_color,  # validate_eye_color,  # Eye Color
    "pid": validate_passport_id,  # validate_passport_id,  # Passport ID
    "cid": validate_cid,  # Country ID
}


def main() -> None:
    """Main"""
    with open(inputfile) as infile:
        raw_data = infile.read()

    passports_raw = raw_data.split("\n\n")

    passports = []
    for passport_raw_data in passports_raw:
        passports.append(parse_passport(passport_raw_data))

    print(f"Count of all passports {len(passports)}")
    valid_passports = part1_count_valid(passports)
    print(f"Part 1: Valid Passports (without cid) == {valid_passports}")

    valid_passports_2 = part2_count_valid(passports)
    print(f"Part 2: Valid Passports (without cid) == {valid_passports_2}")


def part1_count_valid(passports: List[Dict[str, str]]) -> int:
    """Validate part 1 conditions"""
    count = 0
    required_keys = set(k for k, v in fields.items() if k != "cid")
    for passport in passports:
        if all(field in passport for field in required_keys):
            count += 1
    return count


def part2_count_valid(passports: List[Dict[str, str]]) -> int:
    """Validate part 2 conditions"""
    count = 0
    for passport in passports:
        if not all(
            field in passport for field, item in fields.items() if field != "cid"
        ):
            continue
        if all(fn(passport[key]) for key, fn in fields.items() if key != "cid"):
            count += 1
    return count


def parse_passport(data: str) -> Dict[str, str]:
    """Parse passport data and return dictionary"""
    if not data:
        # No data
        return {}

    passport = {}
    entries = data.split()
    for entry in entries:
        entry_key, entry_value = entry.split(":")
        passport[entry_key] = entry_value

    return passport
