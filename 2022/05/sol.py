import sys
import re
from collections import deque


def parse_crates(lines):
    column_names = lines.pop().split()
    num_colums = len(column_names)
    stacks = dict([(name, deque([])) for name in column_names])
    cols_pattern = re.compile(r"(\s{3}|\[.\])\s?" * num_colums)

    for line in lines[::-1]:
        matches = cols_pattern.match(line)
        for stack, crate in zip(column_names, matches.groups()):
            if crate.strip():
                stacks[stack].append(crate[1:-1])
    return stacks


def rearrange_crates(crates, instruction):
    if instruction:
        for _ in range(int(instruction["quantity"])):
            crates[instruction["to"]].append(crates[instruction["from"]].pop())
    return crates


def part_1(fname):
    raw_crates = []
    loaded_crates = False
    instructions = re.compile(
        r"move (?P<quantity>\d+) from (?P<from>\d+) to (?P<to>\d+)"
    )
    for line in open(fname, "r"):
        if not loaded_crates:
            if line.strip():
                raw_crates.append(line)
            else:
                loaded_crates = True
                crates = parse_crates(raw_crates)
            continue
        # print(crates)
        matches = instructions.match(line).groupdict()
        crates = rearrange_crates(crates, matches)
    return "".join([crates[k].pop() for k in sorted(crates.keys())])


def rearrange_crates2(crates, instruction):
    if instruction:
        temp = []
        for _ in range(int(instruction["quantity"])):
            temp.append(crates[instruction["from"]].pop())
        crates[instruction["to"]].extend(temp[::-1])
    return crates


def part_2(fname):
    raw_crates = []
    loaded_crates = False
    instructions = re.compile(
        r"move (?P<quantity>\d+) from (?P<from>\d+) to (?P<to>\d+)"
    )
    for line in open(fname, "r"):
        if not loaded_crates:
            if line.strip():
                raw_crates.append(line)
            else:
                loaded_crates = True
                crates = parse_crates(raw_crates)
            continue
        # print(crates)
        matches = instructions.match(line).groupdict()
        crates = rearrange_crates2(crates, matches)
    return "".join([crates[k].pop() for k in sorted(crates.keys())])


if __name__ == "__main__":
    print(part_1(sys.argv[1]))
    print(part_2(sys.argv[1]))
