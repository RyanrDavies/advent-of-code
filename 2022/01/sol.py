import sys


def part1(fname: str) -> int:

    current_total = 0
    max_total = 0
    for line in open(fname, "r"):
        if line.strip():
            current_total += int(line)
        else:
            max_total = max(max_total, current_total)
            current_total = 0
    max_total = max(max_total, current_total)
    return max_total


def part2(fname: str) -> int:
    elves = {}
    current_elf = 1
    for line in open(fname, "r"):
        if line.strip():
            elves[current_elf] = elves.get(current_elf, 0) + int(line)
        else:
            current_elf += 1
    top_three_total = sum(sorted(elves.values())[-3:])
    return top_three_total


if __name__ == "__main__":
    print("Solution for part 1:")
    print(part1(sys.argv[1]))

    print("Solution for part 2:")
    print(part2(sys.argv[1]))
