import sys
import re
from collections import deque
from typing import NewType

HeightMap = NewType("HeightMap", tuple[complex, complex, dict[complex, int]])


def load_height_map(fname: str) -> HeightMap:
    height_map = {}
    start_position = None
    end_position = None
    for row, line in enumerate(open(fname, "r")):
        for column, height in enumerate(line.strip()):
            if height == "S":
                start_position = complex(column, row)
                height = "a"
            if height == "E":
                end_position = complex(column, row)
                height = "z"
            height_map[complex(column, row)] = ord(height) - 96
    return (start_position, end_position, height_map)


def get_valid_neighbours(
    height_map: dict[complex, int], position: complex
) -> list[complex]:
    current_height = height_map[position]
    valid_neighbours = []
    for dir in [1, -1, 1j, -1j]:
        if height_map.get(position + dir, current_height + 2) <= (current_height + 1):
            valid_neighbours.append(position + dir)
    return valid_neighbours


def find_shortest_path(mapping: HeightMap) -> int:
    start, end, height_map = mapping
    candidates = [start]
    iterations = 0
    dists = {start: []}
    while len(candidates) > 0:
        iterations += 1
        position = candidates.pop(0)
        possible_next_steps = get_valid_neighbours(height_map, position)
        for n in possible_next_steps:
            if n == end:
                return len(dists[position]) + 1
            if (not n in dists.keys()) or (len(dists[position]) + 1 < len(dists[n])):
                dists[n] = dists[position] + [position]
                candidates.append(n)
        candidates.sort(key=lambda x: (len(dists[x]) + (26 - height_map[x])))
    return -1


def part_1(mapping: HeightMap) -> int:
    return find_shortest_path(mapping)


def part_2(mapping: HeightMap) -> int:
    _, end, height_map = mapping
    possible_starts = [p for p, h in height_map.items() if h == 1]
    shortest_path = sys.maxsize
    for s in possible_starts:
        path_length = find_shortest_path((s, end, height_map))
        if path_length > 0:
            shortest_path = min(path_length, shortest_path)
    return shortest_path


if __name__ == "__main__":
    map = load_height_map(sys.argv[1])
    print(part_1(map))
    print(part_2(map))
