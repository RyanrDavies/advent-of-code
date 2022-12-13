import sys
import re
from collections import deque


def load_pairs(fname: str) -> dict[int, list]:
    pair = []
    counter = 1
    output = {}
    for line in open(fname, "r"):
        line = line.strip()
        if line:
            pair.append(eval(line))
        else:
            output[counter] = tuple(pair)
            counter += 1
            pair = []
    if pair:
        output[counter] = tuple(pair)
        counter += 1
    return output


def compare(left, right):
    # print(left, right)
    if left == []:
        if right == []:
            return None
        else:
            return True
    elif right == []:
        return False
    if type(left[0]) == type(right[0]):
        if type(left[0]) == list:
            if compare(left[0], right[0]) is not None:
                return compare(left[0], right[0])
            else:
                return compare(left[1:], right[1:])
        elif type(left[0]) == int:
            if left[0] < right[0]:
                return True
            elif left[0] > right[0]:
                return False
            else:
                return compare(left[1:], right[1:])
    else:
        if type(left[0]) == int:
            return compare([[left[0]]] + left[1:], right)
        else:
            return compare(left, [[right[0]]] + right[1:])


def part_1(pairs):
    # print(compare(*pairs[2]))
    # print(dict([(k, compare(*v)) for k, v in pairs.items()]))
    return sum([k for k, v in sorted(pairs.items()) if compare(*v)])


def part_2(pairs):
    all_pairs = []
    for p1, p2 in pairs.values():
        all_pairs.append(p1)
        all_pairs.append(p2)
    all_pairs.extend([[[2]], [[6]]])
    sorted_list = []
    changes = True
    while changes:
        # print("here")
        changes = False
        for i in range(len(all_pairs) - 1):
            if not compare(all_pairs[i], all_pairs[i + 1]):
                all_pairs = (
                    all_pairs[:i]
                    + [all_pairs[i + 1]]
                    + [all_pairs[i]]
                    + all_pairs[i + 2 :]
                )
                changes = True
    # for ii in all_pairs:
    # print(ii)
    return (all_pairs.index([[2]]) + 1) * (all_pairs.index([[6]]) + 1)


if __name__ == "__main__":
    pairs = load_pairs(sys.argv[1])
    print(part_1(pairs))
    # pairs = load_pairs(sys.argv[1])
    print(part_2(pairs))
