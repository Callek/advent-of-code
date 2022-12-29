"""2020 - Day 2"""
import re
import os

inputfile = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../2020/days/2/input.txt")
)


def main() -> None:
    """Main Logic"""
    with open(inputfile) as infile:
        raw_data = infile.read().splitlines()

    pat = re.compile(r"(?P<min>\d+)-(?P<max>\d+) (?P<char>[a-z]): (?P<password>[a-z]+)")
    count = 0
    count_new = 0

    for line in raw_data:
        if not line:
            continue
        match = pat.match(line)
        if not match:
            raise Exception(f"Huh {line}")

        min_, max_, char, password = match.groups()
        if int(min_) > int(max_):
            raise Exception("Unexpected")
        if not len(char) == 1:
            raise Exception("Unexpected")
        if int(min_) <= password.count(char) <= int(max_):
            # print(f"GOOD {match.groups()}")
            count += 1
        else:
            # print(f"BAD {match.groups()}")
            pass

        # new
        valid = False
        if len(password) >= int(min_) and password[int(min_) - 1] == char:
            valid = True  # for now
        if len(password) >= int(max_) and password[int(max_) - 1] == char and not valid:
            valid = True
        elif len(password) >= int(max_) and password[int(max_) - 1] == char and valid:
            valid = False
        if valid:
            count_new += 1
        # if we're here we didn't find a valid password

    print(f"Total valid passwords old {count}")
    print(f"Total valid passwords new {count_new}")
