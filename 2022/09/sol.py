import sys
from numbers import Number


DIRECTION_LOOKUP = {"U": 1j, "D": -1j, "R": 1, "L": -1}


class Rope:
    def __init__(self, num_knots: int = 2) -> None:
        self.knots = [0j for _ in range(num_knots)]
        self.num_knots = num_knots

    def move_head(self, vector: complex) -> None:
        self.knots[0] += vector
        for knot in range(1, self.num_knots):
            inter_knot_distance = self.knots[knot - 1] - self.knots[knot]
            if abs(inter_knot_distance) > 2**0.5:
                self.knots[knot] += complex(
                    self._sign(inter_knot_distance.real),
                    self._sign(inter_knot_distance.imag),
                )

    def get_tail_position(self) -> complex:
        return self.knots[-1]

    def _sign(self, number: Number) -> Number:
        if number > 0:
            return 1
        if number == 0:
            return 0
        if number < 0:
            return -1

        raise ValueError


def get_number_of_unique_tail_positions_over_time(fname, rope: Rope) -> int:
    tail_positions = set()
    tail_positions.add(rope.get_tail_position())
    for line in open(fname, "r"):
        direction, num_steps = line.split()
        direction_vector = DIRECTION_LOOKUP[direction]
        for _ in range(int(num_steps)):
            rope.move_head(direction_vector)
            tail_positions.add(rope.get_tail_position())
    # print(tail_positions)
    # s = list()
    # for y in range(4, -1, -1):
    #     for x in range(6):
    #         if complex(x, y) in set(tail_positions):
    #             s.append("#")
    #         else:
    #             s.append(".")
    #     s.append("\n")
    # print("".join(s))
    return len(tail_positions)


def part_1(fname):
    rope = Rope(num_knots=2)
    return get_number_of_unique_tail_positions_over_time(fname, rope)


def part_2(fname):
    rope = Rope(num_knots=10)
    return get_number_of_unique_tail_positions_over_time(fname, rope)


if __name__ == "__main__":

    print(part_1(sys.argv[1]))
    print(part_2(sys.argv[1]))
