from typing import Optional, Tuple

from utils.decorators import time_it
from utils.helper_functions import (
    read_input,
    read_input_lines,
    read_input_int,
    read_input_int_individuals,
    read_input_int_matrix, add_pos
)
import numpy as np

INPUT_FILENAME = "aoc/day_12/INPUT.txt"
EXAMPLE_FILENAME = "aoc/day_12/EXAMPLE_01.txt"


MOVES = {
    "up": (0, -1),
    "right": (1, 0),
    "down": (0, 1),
    "left": (-1, 0),
}


def in_range(pos, matrix):
    if 0 <= pos[0] < len(matrix) and 0 <= pos[1] < len(matrix[0]):
        return True
    else:
        return False


def calculate_possible_moves(matrix):
    ylen = len(matrix)
    xlen = len(matrix[0])
    possible_moves = [ [0]*xlen for i in range(ylen)]

    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            pos = (y, x)
            char = matrix[y][x]
            value = get_value(char)
            for key, move in MOVES.items():
                new_pos = add_pos(pos, move)
                if in_range(new_pos, matrix):
                    possible_move = is_possible_move(pos, new_pos, matrix)
                    if possible_move:
                        if possible_moves[y][x]:
                            possible_moves[y][x].append(key)
                        else:
                            possible_moves[y][x] = [key]
    return possible_moves


def get_start_pos(matrix) -> Optional[Tuple]:
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == "S":
                return (y,x)
    return None


def get_value(c: str):
    if c == "S":
        return 1
    elif c == "E":
        return 26
    if c.islower():
        return ord(c) - 96  # a = 1, z = 26
    else:
        return ord(c) - 38  # A = 27


def is_possible_move(a, b, matrix):
    value_a = get_value(matrix[a[0]][a[1]])
    value_b = get_value(matrix[b[0]][b[1]])
    return np.abs(value_a - value_b) <= 1


@time_it
def solve_part_1():

    print("Day 12 - Part 1")
    lines = read_input_lines(EXAMPLE_FILENAME, True)
    start = get_start_pos(lines)
    possible_moves = calculate_possible_moves(lines)
    print(lines)


def best_path(possible_moves, matrix, pos, goal, visited=None):

    # 1. Starting from S
    # 2. Go through each possible move in a new recursion. Return the minimum value of all of those
    # 3. Stop each recursion if:
        # a) hitting a position you've already seen
        # b) finding the exit
    # 4. Return total cost ( Each step costs 1 )

    for move in possible_moves[pos[0]][pos[1]]:
        if
        costs =


    return min(best_path(possible_moves, matrix, pos))



@time_it
def solve_part_2():
    print("Day 12 - Part 2")


if __name__ == "__main__":
    solve_part_1()
    # solve_part_2()