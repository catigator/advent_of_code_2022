import copy
from typing import Optional, Tuple, List

from utils.decorators import time_it
from utils.helper_functions import (
    read_input,
    read_input_lines,
    read_input_int,
    read_input_int_individuals,
    read_input_int_matrix, add_pos, print_matrix
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

REVERSE_MOVES = {
    "up": "down",
    "right": "left",
    "down": "up",
    "left": "right",
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
    return get_pos_for_char(matrix, "S")


def get_end_pos(matrix) -> Optional[Tuple]:
    return get_pos_for_char(matrix, "E")

def get_pos_for_char(matrix, char) -> Optional[Tuple]:
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] == char:
                return (y, x)
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


def get_min_path_from_list(possible_paths: Tuple[List, int]):
    """
    possible_paths = [ [path: Lost, cost] ]
    """
    return min(possible_paths, key=lambda path_cost_tuple: path_cost_tuple[1])


def get_best_path(possible_moves, matrix, pos, goal, current_path=None, cost=0):
    """

    """

    # 1. Starting from S
    # 2. Go through each possible move in a new recursion. Return the minimum value of all of those
    # 3. Stop each recursion if:
    #       a) hitting a position you've already seen
    #       b) finding the exit
    # 4. Return total cost ( Each step costs 1 )
    if current_path is None:
        current_path = []

    possible_paths = []
    for move_str in possible_moves[pos[0]][pos[1]]:
        new_cost = cost
        move = MOVES[move_str]
        new_pos = add_pos(pos, move)
        if is_possible_move(pos, new_pos, matrix) and new_pos not in current_path:
            new_cost += 1
            new_path = copy.deepcopy(current_path)
            new_path.append(new_pos)

            if matrix[new_pos[0]][new_pos[1]] == "E":
                possible_paths.append([new_path, cost])
            else:
                new_best_path = get_best_path(possible_moves, matrix, new_pos, goal, new_path, new_cost)
                if new_best_path is not None:
                    possible_paths.append(new_best_path)
    if possible_paths != []:
        min_path_cost_tuple = get_min_path_from_list(possible_paths)
        return min_path_cost_tuple
    else:
        return None


def print_moves(best_path, matrix):
    path_matrix = np.zeros((len(matrix), len(matrix[0])))
    for i, pos in enumerate(best_path):
        path_matrix[pos[0]][pos[1]] = i
    print(path_matrix)
    print("---------")
    print_matrix(matrix)
    return path_matrix


@time_it
def solve_part_1():

    print("Day 12 - Part 1")
    lines = read_input_lines(EXAMPLE_FILENAME, True)
    start_pos = get_start_pos(lines)
    end_pos = get_end_pos(lines)
    possible_moves = calculate_possible_moves(lines)
    best_path, cost = get_best_path(possible_moves, lines, start_pos, end_pos)
    print_moves(best_path, lines)
    print(f"The lowest cost was {cost}")
    print(lines)



@time_it
def solve_part_2():
    print("Day 12 - Part 2")


if __name__ == "__main__":
    solve_part_1()
    # solve_part_2()