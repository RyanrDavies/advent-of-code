import sys


def lookup_priority(chr):
    return (ord(chr) - 96) % 58


def part_1(fname):
    total = 0
    for line in open(fname, "r"):
        line = line.strip()
        assert len(line) % 2 == 0
        halfway = int(len(line) / 2)
        first_compartment = set(line[:halfway])
        second_compartment = set(line[halfway:])
        shared_item_type = first_compartment.intersection(second_compartment).pop()
        total += lookup_priority(shared_item_type)
    return total


def part_2(fname):
    total = 0
    group_rucksacks = []
    for line in open(fname, "r"):
        group_rucksacks.append(set(line.strip()))
        if len(group_rucksacks) < 3:
            continue
        common_item = (
            group_rucksacks[0]
            .intersection(group_rucksacks[1])
            .intersection(group_rucksacks[2])
            .pop()
        )
        total += lookup_priority(common_item)
        group_rucksacks = []
    return total


if __name__ == "__main__":
    print(part_1(sys.argv[1]))
    print(part_2(sys.argv[1]))
