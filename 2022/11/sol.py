import sys
import re
from collections import deque
from typing import Callable, Self


class Monkey:
    def __init__(
        self,
        id: int,
        # items: list[int],
        operation: Callable,
        test_divisor: int,
        next_monkey_true: int,
        next_monkey_false: int,
    ) -> None:

        self.id = id
        self.items = deque([])
        self.operation = operation
        self.test_divisor = test_divisor
        self.next_monkey_true = next_monkey_true
        self.next_monkey_false = next_monkey_false
        self.items_inspected = 0

    def inspect_item(self, worrying: bool) -> tuple[int, int]:
        self.items_inspected += 1
        item = self.items.popleft()
        item = self.operation(item)
        # if not worrying:
        # item = int(item / 3)
        if self.test_item(item):
            return (self.next_monkey_true, item)
        else:
            return (self.next_monkey_false, item)

    def catch_item(self, item: int) -> None:
        self.items.append(item)

    def test_item(self, item: int) -> bool:
        return item.modulos[self.test_divisor] == 0


class Item:
    def __init__(self, initial_value: int, modulos: list[int]) -> None:
        self.modulos = {}
        for m in modulos:
            self.modulos[m] = initial_value % m

    def __add__(self, other_val):
        if type(other_val) == int:
            for m in self.modulos.keys():
                self.modulos[m] = (self.modulos[m] + (other_val % m)) % m
        return self

    def __add__(self, other_val) -> Self:
        if type(other_val) == int:
            for m in self.modulos.keys():
                self.modulos[m] = (self.modulos[m] + (other_val % m)) % m
        else:
            raise TypeError
        return self

    def __mul__(self, other_val) -> Self:
        if type(other_val) == int:
            for m in self.modulos.keys():
                self.modulos[m] = (self.modulos[m] * (other_val % m)) % m
        elif type(other_val) == type(self):
            for m in self.modulos.keys():
                self.modulos[m] = (self.modulos[m] * (other_val.modulos[m])) % m
        else:
            raise TypeError
        return self


def load_monkeys(fname: str) -> list[Monkey]:
    monkeys = []
    monkey_params = {}
    monkey_items = {}
    for line in open(fname, "r"):

        line = line.strip()
        if line:
            if line[0] == "M":
                monkey_params["id"] = int(line.split()[1][:-1])
            else:
                parameter, value = line.split(":")
                if parameter == "Starting items":
                    monkey_items[monkey_params["id"]] = [
                        int(i) for i in value.split(", ")
                    ]
                elif parameter == "Operation":
                    monkey_params["operation"] = eval(
                        "lambda old: " + value.split("=")[-1]
                    )
                elif parameter == "Test":
                    monkey_params["test_divisor"] = int(value.split()[-1])
                elif parameter == "If true":
                    monkey_params["next_monkey_true"] = int(value.split()[-1])
                elif parameter == "If false":
                    monkey_params["next_monkey_false"] = int(value.split()[-1])
        else:
            monkeys.append(Monkey(**monkey_params))
            monkey_params = {}
    if monkey_params:
        monkeys.append(Monkey(**monkey_params))

    modulo_values = [m.test_divisor for m in monkeys]
    for m in monkeys:
        for v in monkey_items[m.id]:
            m.catch_item(Item(v, modulo_values))

    return sorted(monkeys, key=lambda x: x.id)


def run_round(monkeys: list[Monkey], worrying: bool) -> list[Monkey]:
    for monkey in monkeys:
        while len(monkey.items) > 0:
            next_monkey, item = monkey.inspect_item(worrying)
            monkeys[next_monkey].catch_item(item)
    return monkeys


def run_rounds(
    monkeys: list[Monkey], num_rounds: int, worrying: bool, print_every: int = 1
) -> list[Monkey]:
    for r in range(num_rounds):
        monkeys = run_round(monkeys, worrying)
        if r % print_every == 0:
            print(f"After round {r+1}:")
            for m in monkeys:
                print(f"\tMonkey {m.id}: {m.items_inspected}")
            sys.stdout.flush()
    return monkeys


def part_1(monkeys: list[Monkey]) -> int:
    monkeys = run_rounds(monkeys, 20, False)
    monkeys.sort(key=lambda x: x.items_inspected * -1)
    return monkeys[0].items_inspected * monkeys[1].items_inspected


def part_2(monkeys: list[Monkey]) -> int:
    monkeys = run_rounds(monkeys, 10000, True, print_every=999)
    monkeys.sort(key=lambda x: x.items_inspected * -1)
    return monkeys[0].items_inspected * monkeys[1].items_inspected


if __name__ == "__main__":
    monkeys = load_monkeys(sys.argv[1])
    # print(monkeys)
    # print(part_1(load_monkeys(sys.argv[1])))
    print(part_2(load_monkeys(sys.argv[1])))
