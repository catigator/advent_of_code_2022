from dataclasses import dataclass
from typing import List

from utils.decorators import time_it
from utils.helper_functions import (
    read_input,
    read_input_lines,
    read_input_int,
    read_input_int_individuals,
    read_input_int_matrix, read_input_split_on_empty_line
)
import numpy as np


INPUT_FILENAME = "aoc/day_11/INPUT.txt"
EXAMPLE_FILENAME = "aoc/day_11/EXAMPLE_01.txt"


@dataclass
class Monkey:
    monkey: int
    items: List[int]
    operator: str
    actor: str
    test: int
    true: int
    false: int


def test_item(monkey, item_index):
    if monkey.items[item_index] % monkey.test == 0:
        return True
    else:
        return False

def get_bored(monkey, item_index):
    monkey.items[item_index] = np.floor(monkey.items[item_index] / 3.0)
    return monkey

def get_monkey_to_throw_to(monkey, item_index) -> int:
    if test_item(monkey, item_index):
        return monkey.true
    else:
        return monkey.false


def add_item(monkeys: List[Monkey], monkey_num: int, item):
    monkeys[monkey_num].items.append(item)


def inspect_item(monkey, item_index):
    if monkey.operator == "+":
        if monkey.actor == "old":
            monkey.items[item_index] += monkey.items[item_index]
        else:
            monkey.items[item_index] += int(monkey.actor)
    elif monkey.operator == "*":
        if monkey.actor == "old":
            monkey.items[item_index] *= monkey.items[item_index]
        else:
            monkey.items[item_index] *= int(monkey.actor)
    return monkey


def process_monkeys(monkeys: List[Monkey]):
    rounds = 20
    for n in range(rounds):
        for monkey in monkeys:
            for item_index in range(len(monkey.items)):
                monkey = inspect_item(monkey, item_index)
                monkey = get_bored(monkey, item_index)
                which_monkey = get_monkey_to_throw_to(monkey, item_index)
                add_item(monkeys, which_monkey, monkey.items[item_index])
                a = 1
            monkey.items = []

    return monkeys


def read_monkeys(lines):
    monkeys = []

    for i, line in enumerate(lines):
        monkey = int(line[0][7])
        starting_items = [int(x) for x in line[1][16:].split(", ")]
        operator = line[2][21]
        actor = line[2][23:]
        test = int(line[3][19:])
        true = int(line[4][25])
        false = int(line[5][26])

        new_monkey = Monkey(
            monkey=monkey,
            items=starting_items,
            operator=operator,
            actor=actor,
            test=test,
            true=true,
            false=false,
        )
        monkeys.append(new_monkey)
    return monkeys


def process_lines(lines):

    monkeys = read_monkeys(lines)
    monkeys = process_monkeys(monkeys)

    return None


@time_it
def solve_part_1():
    print("Day 11 - Part 1")
    lines = read_input_split_on_empty_line(EXAMPLE_FILENAME)
    results = process_lines(lines)
    print(lines)

@time_it
def solve_part_2():
    print("Day 11 - Part 2")


if __name__ == "__main__":
    solve_part_1()
    # solve_part_2()