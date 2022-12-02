from typing import Tuple

from utils.decorators import time_it
from utils.helper_functions import (
    read_input,
    read_input_lines,
    read_input_int,
    read_input_int_individuals,
    read_input_int_matrix
)


INPUT_FILENAME = "aoc/day_02/INPUT.txt"
EXAMPLE_FILENAME = "aoc/day_02/EXAMPLE_01.txt"

# Points per shape
SHAPE = {
    "R": 1,
    "P": 2,
    "S": 3
}

# Score for winning, losing or drawing between OUTCOME[player][opponent]
OUTCOME = {
    "R": {
        "R": 3,
        "P": 0,
        "S": 6,
    },
    "P": {
            "R": 6,
            "P": 3,
            "S": 0,
        },
    "S": {
            "R": 0,
            "P": 6,
            "S": 3,
        }
}

# For a given opponent move as key, lists the moves required to (Win, Lose, Draw)
TO_WIN_LOSE_DRAW = {
    "R": ("P", "S", "R"),
    "P": ("S", "R", "P"),
    "S": ("R", "P", "S"),
}

# Returns index to use in TO_WIN_LOSE_DRAW. (0 = Win, 1 = Lose, 2 = Draw)
# Would likely be easier to read if the format was reordered to match the description inputs:
# "X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win."
# i.e. (0 = Lose, 1 = Draw, 3 = Win). But ¯\_(ツ)_/¯ too lazy to change TO_WIN_LOSE_DRAW format now.
WLD_COMMAND = {
    "X": 1,
    "Y": 2,
    "Z": 0
}

# Converts from input to "R"ock, "P"aper, "S"cissors
CONV = {
    "A": "R",
    "B": "P",
    "C": "S",
    "X": "R",
    "Y": "P",
    "Z": "S",
}


def outcome(command: Tuple[int]):
    player = CONV[command[1]]
    elf = CONV[command[0]]

    result = OUTCOME[player][elf] + SHAPE[player]
    return result


def outcome_2(command: Tuple[int]):
    wld_command = WLD_COMMAND[command[1]]
    elf = CONV[command[0]]
    player = TO_WIN_LOSE_DRAW[elf][wld_command]

    result = OUTCOME[player][elf] + SHAPE[player]
    return result


@time_it
def solve_part_1():
    print("Day 02 - Part 1")
    lines = read_input_lines(INPUT_FILENAME, strip_whitespace=True)
    commands = [line.split() for line in lines]
    total_score = sum([outcome(command) for command in commands])
    print(f"The total score was {total_score}")


@time_it
def solve_part_2():
    print("Day 02 - Part 2")
    lines = read_input_lines(INPUT_FILENAME, strip_whitespace=True)
    commands = [line.split() for line in lines]
    total_score = sum([outcome_2(command) for command in commands])
    print(f"The total score was {total_score}")


if __name__ == "__main__":
    solve_part_1()
    solve_part_2()