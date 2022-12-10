import sys
from collections import deque


class CPU:
    def __init__(self) -> None:
        self.register_x = 1
        self.cycle = 1
        self.queue = deque([])

    def step(self) -> None:
        self.cycle += 1
        self.register_x += self.queue.popleft()

    def add_instruction(self, instruction: str) -> None:
        if instruction == "noop":
            self.queue.append(0)
            return
        command, argument = instruction.split()
        if command == "addx":
            self.queue.append(0)
            self.queue.append(int(argument))
            return


def part_1(fname: str) -> int:
    cycle_of_interest = 20
    signal_strengths = []
    cpu = CPU()
    for line in open(fname, "r"):
        line = line.strip()
        cpu.add_instruction(line)
    while len(cpu.queue) > 0:
        cpu.step()
        if cycle_of_interest == cpu.cycle:
            signal_strengths.append(cycle_of_interest * cpu.register_x)
            cycle_of_interest += 40

    print(signal_strengths)
    return sum(signal_strengths)


def part_2(fname: str) -> str:
    crt_rows = []
    crt_row = []
    cpu = CPU()
    for line in open(fname, "r"):
        line = line.strip()
        cpu.add_instruction(line)
    while len(cpu.queue) > 0:
        print(cpu.cycle % 40, (cpu.register_x - 1, cpu.register_x + 1))
        if (cpu.register_x - 1) <= (cpu.cycle - 1) % 40 <= (cpu.register_x + 1):
            crt_row.append("#")
        else:
            crt_row.append(".")
        cpu.step()
        if (cpu.cycle - 1) % 40 == 0:
            crt_rows.append("".join(crt_row))
            crt_row = []
    return "\n".join(crt_rows)


if __name__ == "__main__":

    print(part_1(sys.argv[1]))
    print(part_2(sys.argv[1]))
