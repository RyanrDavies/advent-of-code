import sys
import re
from collections import deque, defaultdict


class Tree:
    def __init__(self, height):
        self.height = int(height)
        self.visible = False

    def __lt__(self, other: object) -> bool:
        return self.height < other

    def __gt__(self, other: object) -> bool:
        return self.height > other

    def __le__(self, other: object) -> bool:
        return self.height <= other

    def __ge__(self, other: object) -> bool:
        return self.height >= other

    def __eq__(self, other: object) -> bool:
        return self.height == other

    def set_visible(self):
        self.visible = True


class Forest:
    def __init__(self, grid):
        self.trees = defaultdict(dict)
        for row in range(len(grid)):
            for column in range(len(grid[0])):
                self.trees[row][column] = grid[row][column]
        self.num_rows = len(grid)
        self.num_columns = len(grid[0])

    def mark_visible(self):
        for r in range(self.num_rows):
            max_height_seen = -1
            self.trees[r][0].set_visible()
            max_height_seen = self.trees[r][0].height
            for c in range(1, self.num_columns):
                if self.trees[r][c] > max_height_seen:
                    self.trees[r][c].set_visible()
                    max_height_seen = self.trees[r][c].height

            max_height_seen = -1
            self.trees[r][self.num_columns - 1].set_visible()
            max_height_seen = self.trees[r][self.num_columns - 1].height
            for c in range(self.num_columns - 1, 0, -1):
                if self.trees[r][c] > max_height_seen:
                    self.trees[r][c].set_visible()
                    max_height_seen = self.trees[r][c].height

        for c in range(self.num_columns):
            max_height_seen = -1
            self.trees[0][c].set_visible()
            max_height_seen = self.trees[0][c].height
            for r in range(1, self.num_rows):
                if self.trees[r][c] > max_height_seen:
                    self.trees[r][c].set_visible()
                    max_height_seen = self.trees[r][c].height

            max_height_seen = -1
            self.trees[self.num_rows - 1][c].set_visible()
            max_height_seen = self.trees[self.num_rows - 1][c].height
            for r in range(self.num_rows - 1, 0, -1):
                if self.trees[r][c] > max_height_seen:
                    self.trees[r][c].set_visible()
                    max_height_seen = self.trees[r][c].height

    def count_visible(self):
        count = 0
        for i in range(self.num_rows):
            count += sum([t.visible for t in self.trees[i].values()])
        return count

    def __repr__(self) -> str:
        string = ""
        char_lookup = {True: "|", False: "."}
        for r in range(self.num_rows):
            for c in range(self.num_columns):
                string += char_lookup[self.trees[r][c].visible]
            string += "\n"
        return string

    def scenic_score(self, row, column):
        this_tree = self.trees[row][column]

        # going north
        count_north = 0
        for r in range(row - 1, 0 - 1, -1):
            count_north += 1
            if self.trees[r][column] >= this_tree:
                break

        # going south
        count_south = 0
        for r in range(row + 1, self.num_rows, 1):
            count_south += 1
            if self.trees[r][column] >= this_tree:
                break

        # going east
        count_east = 0
        for c in range(column + 1, self.num_columns, 1):
            count_east += 1
            if self.trees[row][c] >= this_tree:
                break

        # going west
        count_west = 0
        for c in range(column - 1, 0 - 1, -1):
            count_west += 1
            if self.trees[row][c] >= this_tree:
                break

        return count_north * count_south * count_east * count_west


def load_forest(fname):
    forest = []
    for line in open(fname, "r"):
        forest.append([Tree(i) for i in line.strip()])
    return forest


def part_1(forest):
    f = Forest(forest)
    f.mark_visible()
    return f.count_visible()


def part_2(forest):
    f = Forest(forest)
    max_score = 0
    for r in range(f.num_rows):
        for c in range(f.num_columns):
            max_score = max(max_score, f.scenic_score(r, c))
    return max_score


if __name__ == "__main__":

    forest = load_forest(sys.argv[1])

    print(part_1(forest))
    print(part_2(forest))
