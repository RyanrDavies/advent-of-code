class CPU:
    def __init__(self) -> None:
        self.register_x = 1
        self.cycle = 0

    def perform_instruction(self, instruction: str) -> None:
        if instruction == "noop":
            self.cycle += 1
            return
        command, argument = instruction.split()
        if command == "addx":
            self.cycle += 2
            self.register_x += int(argument)


def part_1(fname):
    cycle_of_interest = 20
    signal_strengths = []
    cpu = CPU()
    for line in open(fname, "r"):
        line = line.strip()
        current_cycle_value_pair = (cpu.cycle, cpu.register_x)
        cpu.perform_instruction(line)
        if current_cycle_value_pair[0] <= cycle_of_interest <= cpu.cycle:
            signal_strengths.append(cycle_of_interest * current_cycle_value_pair[1])
            cycle_of_interest += 40
    return sum(signal_strengths)
