import sys
import regex as re


def part_1(fname):
    count = 0
    re_parser = re.compile(r"^(\d+)-(\d+),(\d+)-(\d+)\s*")
    for line in open(fname, "r"):
        matches = re_parser.match(line).groups()
        elf1_start, elf1_end, elf2_start, elf2_end = tuple(map(int, matches))
        if (elf1_start <= elf2_start and elf1_end >= elf2_end) or (
            elf2_start <= elf1_start and elf2_end >= elf1_end
        ):
            count += 1
    return count


def part_2(fname):
    count = 0
    re_parser = re.compile(r"^(\d+)-(\d+),(\d+)-(\d+)\s*")
    for line in open(fname, "r"):
        matches = re_parser.match(line).groups()
        elf1_start, elf1_end, elf2_start, elf2_end = tuple(map(int, matches))
        if elf2_start <= elf1_end and elf2_end >= elf1_start:
            count += 1
    return count


if __name__ == "__main__":
    print(part_1(sys.argv[1]))
    print(part_2(sys.argv[1]))
