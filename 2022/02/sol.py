import sys

OUTCOME_POINTS = {
    0: {0: 3, 1: 6, 2: 0},
    1: {0: 0, 1: 3, 2: 6},
    2: {0: 6, 1: 0, 2: 3},
}

SHAPE_POINTS = {
    0: 1,
    1: 2,
    2: 3,
}

DECODE_OPPONENT = {
    "A": 0,
    "B": 1,
    "C": 2,
}

DECODE_MINE = {
    "X": 0,
    "Y": 1,
    "Z": 2,
}


def part_1(fname):
    total_score = 0
    for line in open(fname, "r"):
        opponent_move, my_move = line.split()
        opponent_move = DECODE_OPPONENT[opponent_move]
        my_move = DECODE_MINE[my_move]
        round_score = OUTCOME_POINTS[opponent_move][my_move] + SHAPE_POINTS[my_move]
        total_score += round_score
    return total_score


DECODE_OUTCOMES = {
    "X": (-1, 0),
    "Y": (0, 3),
    "Z": (1, 6),
}


def part_2(fname):
    total_score = 0
    for line in open(fname, "r"):
        opponent_move, outcome = line.split()
        opponent_move = DECODE_OPPONENT[opponent_move]
        outcome_offset, outcome_points = DECODE_OUTCOMES[outcome]
        move_index = (opponent_move + outcome_offset) % 3
        my_move = [0, 1, 2][move_index]
        round_score = outcome_points + SHAPE_POINTS[my_move]
        total_score += round_score
    return total_score


if __name__ == "__main__":
    print(part_1(sys.argv[1]))
    print(part_2(sys.argv[1]))
