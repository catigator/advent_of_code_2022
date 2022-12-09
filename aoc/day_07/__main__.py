from __future__ import annotations
from collections import defaultdict
from dataclasses import dataclass
from typing import List, Set, Optional

from utils.decorators import time_it
from utils.helper_functions import (
    read_input,
    read_input_lines,
    read_input_int,
    read_input_int_individuals,
    read_input_int_matrix
)


INPUT_FILENAME = "aoc/day_07/INPUT.txt"
EXAMPLE_FILENAME = "aoc/day_07/EXAMPLE_02.txt"


@dataclass
class Directory:
    directories: Optional[defaultdict[Directory]]
    files: Optional[defaultdict[int]]
    size: Optional[int]
    up: Optional[Directory]
    level: Optional[int]
    name: str

ROOT_DIRECTORY = Directory(defaultdict(Directory), defaultdict(int), None, None, 0, "/")


def get_size_files(files: defaultdict[int]):
    size = 0
    for key, value in files.items():
        size += int(value)
    return size


def get_size_directory(directory, small_dirs: List, min_num=True):
    size = 0
    for sub_dir_name, sub_dir in directory.directories.items():
        extra_size, small_dirs = get_size_directory(sub_dir, small_dirs, min_num)
        size += extra_size
    size += get_size_files(directory.files)
    directory.size = size
    if min_num:
        if size < 100000:
            small_dirs.append(directory)
    else:
        small_dirs.append(directory)
    return size, small_dirs

def maybe_add_new_directory(current_dir: Directory, dir_name) -> bool:
    if dir_name in current_dir.directories:
        return False
    else:
        new_dir = Directory(defaultdict(Directory), defaultdict(Directory), None, current_dir, current_dir.level + 1, dir_name)
        current_dir.directories[dir_name] = new_dir
        return True


def maybe_add_new_file(current_dir: Directory, size: int, filename: str) -> bool:
    if filename in current_dir.files:
        return False
    else:
        current_dir.files[filename] = size
        return True


def handle_cd(current_dir, dest, start_dir) -> Directory:
    if dest == "..":
        return current_dir.up
    elif dest == "/":
        return start_dir
    elif dest in current_dir.directories:
        return current_dir.directories[dest]
    return None


def handle_ls(current_dir, lines, line_index) -> int:
    new_line_index = line_index

    for i in range(line_index + 1, len(lines)):
        new_line_index = i
        line = lines[i]
        elements = line.split()
        if elements[0] == "$":
            break
        elif elements[0] == "dir":
            new_directory = maybe_add_new_directory(current_dir, elements[1])
            if not new_directory:
                break
        else:
            new_file = maybe_add_new_file(current_dir, elements[0], elements[1])
            if not new_file:
                break
    return new_line_index


def parse_lines(lines, start_dir) -> Directory:
    current_dir = start_dir
    line_index = 0
    while line_index < len(lines) - 1:
        line_index, current_dir = parse_line(lines, line_index, current_dir, start_dir)
    return current_dir


def parse_line(lines, line_index, current_dir, start_dir) -> (int, Directory):
    """
    Example format for lines:

        $ cd /
        $ ls
        dir a
        14848514 b.txt
        8504156 c.dat
        dir d

    """
    elements = lines[line_index].split()

    if elements[0] == "$":
        if elements[1] == "ls":
            return handle_ls(current_dir, lines, line_index), current_dir
        if elements[1] == "cd":
            dest = elements[2]
            current_dir = handle_cd(current_dir, dest, start_dir)
            return line_index + 1, current_dir

    return None, None


def print_dir(dir: Directory):
    dir_tabs = " "*dir.level
    file_tabs = dir_tabs + " "

    print(dir_tabs + "- " + dir.name + " (dir) (size=" + str(dir.size) +")")

    for sub_dir_name, sub_dir in dir.directories.items():
        print_dir(sub_dir)

    for filename, size in dir.files.items():
        print(file_tabs + "- " + filename + "(file, size=" + size + ")")


@time_it
def solve_part_1():
    print("Day 07 - Part 1")
    lines = read_input_lines(INPUT_FILENAME, True)
    start_dir = ROOT_DIRECTORY
    current_dir = parse_lines(lines, start_dir)
    small_dirs = []
    total_size, small_dirs = get_size_directory(start_dir, small_dirs)
    print_dir(start_dir)
    print(f"Size of small dirs is {sum([d.size for d in small_dirs])}")
    a = 1


@time_it
def solve_part_2():
    print("Day 07 - Part 2")
    lines = read_input_lines(INPUT_FILENAME, True)
    start_dir = Directory(defaultdict(Directory), defaultdict(int), None, None, 0, "/")
    current_dir = parse_lines(lines, start_dir)
    small_dirs = []
    total_size, small_dirs = get_size_directory(start_dir, small_dirs, False)
    size_needed = 30000000 - (70000000 - total_size)
    small_dirs.sort(key=lambda dir: dir.size)
    for dir in small_dirs:
        if dir.size > size_needed:
            print(f"Need to delete {dir.name} to free up {dir.size}")
            break
    print(f"Size of small dirs is {sum([d.size for d in small_dirs])}")


if __name__ == "__main__":
    solve_part_1()
    solve_part_2()