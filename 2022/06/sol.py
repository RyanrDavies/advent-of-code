import sys
import re
from collections import deque

EXAMPLES = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
]


def part_1(buffer):
    four_characters = deque(buffer[:4], 4)
    if len(set(four_characters)) == 4:
        return 4
    for index in range(4, len(buffer)):
        four_characters.append(buffer[index])
        if len(set(four_characters)) == 4:
            return index + 1
    return -1


def part_2(buffer):
    fourteen_characters = deque(buffer[:14], 14)
    if len(set(fourteen_characters)) == 14:
        return 14
    for index in range(14, len(buffer)):
        fourteen_characters.append(buffer[index])
        if len(set(fourteen_characters)) == 14:
            return index + 1
    return -1


def test_func(function, outputs):
    for inp, out in zip(EXAMPLES, outputs):
        print(f"{inp} : {function(inp)} | {out}")
        assert function(inp) == out


def test_part_1():
    print("part 1")
    part_1_outs = [7, 5, 6, 10, 11]
    test_func(part_1, part_1_outs)


def test_part_2():
    print("part 2")
    part_2_outs = [19, 23, 23, 29, 26]
    test_func(part_2, part_2_outs)


if __name__ == "__main__":
    if sys.argv[1] == "test":
        test_part_1()
        test_part_2()
    else:
        with open(sys.argv[1], "r") as f:
            line = f.read()
        print(part_1(line))
        print(part_2(line))
