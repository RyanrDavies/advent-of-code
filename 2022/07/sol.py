import sys
import re
from collections import deque


class FileSystem:
    def __init__(self):
        self.current_directory = deque(["/"])
        self.tree = {"/": {}}

    def fill_in_contents(self, contents):
        local_tree = self.tree
        for d in self.current_directory:
            local_tree = local_tree[d]
        for l in contents:
            info, name = l.split()
            if info == "dir":
                local_tree[name] = {}
            else:
                local_tree[name] = int(info)

    def change_directory(self, directory):
        if directory == "/":
            self.current_directory = deque(["/"])
        elif directory == "..":
            self.current_directory.pop()
        else:
            self.current_directory.append(directory)


def get_sizes(tree, record):
    total = 0
    stack = deque(tree.keys())
    while stack:
        item = stack.pop()
        if type(tree[item]) == int:
            total += tree[item]
        else:
            dir_size, record = get_sizes(tree[item], record)
            record.append((item, dir_size))
            total += dir_size
    return total, record


def build_filesystem(fname):
    filesystem = FileSystem()
    current_directory = ""
    command = None
    output = []
    state = ()
    for line in open(fname, "r"):
        if line[0] == "$":
            if output:
                if command == "ls":
                    filesystem.fill_in_contents(output)
            output = []
            command = line[2:].strip()
            if command[:2] == "cd":
                filesystem.change_directory(command[3:])
                command = None
        else:
            output.append(line.strip())
    if output:
        if command == "ls":
            filesystem.fill_in_contents(output)
    return filesystem


def part_1(fname):
    filesystem = build_filesystem(fname)
    all_sizes = []
    get_sizes(filesystem.tree, all_sizes)
    return sum(filter(lambda x: x <= 100000, [b for _, b in all_sizes]))


def part_2(fname):
    filesystem = build_filesystem(fname)
    all_sizes = []
    get_sizes(filesystem.tree, all_sizes)

    total_space = 70000000
    target_space = 30000000
    free_space = total_space - dict(all_sizes)["/"]
    space_to_free = target_space - free_space
    return min(filter(lambda x: x >= space_to_free, [b for _, b in all_sizes]))


if __name__ == "__main__":

    print(part_1(sys.argv[1]))
    print(part_2(sys.argv[1]))
