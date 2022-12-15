from typing import List


def read_input(filename: str) -> str:
    """

    :param filename: Path of file from working directory (e.g. INPUT_FILENAME)
    :return: the contents of the file as a string
    """

    with open(filename) as f:
        input_str = f.read()

    return input_str


def read_input_lines(filename: str, strip_whitespace: bool=False) -> List[str]:
    """

    :param filename:
    :param strip_whitespace:
    :return: A list of all of the lines in file contents as strings

    Output examples:

    [["I am stripped of my whitespace."]]
    [[" I am not stripped of my whitespace.\n"]]
    """
    lines_list = []

    with open(filename) as f:
        lines_list = f.readlines()

    if strip_whitespace:
        lines_list = [line.strip() for line in lines_list]

    return lines_list


def read_input_lines_strip_newline(filename: str):
    lines = read_input_lines(filename)
    stripped_lines = [line.strip("\n") for line in lines]
    return stripped_lines


def read_input_int(filename: str) -> List[int]:
    """

    :param filename: Path of file from working directory
    :return: Each line in file converted to an int and added to a list

    Input example:

    123
    456
    789

    Output example:

    [123, 456, 789]

    """
    lines_list = read_input_lines(filename)

    numbers = [int(line) for line in lines_list]

    return numbers


def read_input_int_individuals(filename: str) -> list:
    """
    Reads a file and returns all numbers in file as separated by commas

    :param filename: Path of file from working directory
    :return: List of all numbers in file

    Input example:

    123,456,789

    Output example:

    [123, 456, 789]
    """
    input_line = read_input(filename)

    numbers = [int(number) for number in input_line.split(",")]

    return numbers


def read_input_split_on_empty_line(filename: str) -> list:
    """
    Reads a file and returns all numbers in file as separated by commas

    Example input:

    a
    a

    b
    b
    b

    Example output:

    [
        [a
        a],

        [b
        b
        b]
    ]
    """
    lines = read_input_lines(filename, True)
    split_lines = []
    temp = []
    for line in lines:
        if line != "":
            temp.append(line)
        else:
            split_lines.append(temp)
            temp = []
    if temp != []:
        split_lines.append(temp)
    return split_lines

def read_input_int_split_on_empty_line(filename: str) -> list:
    """
    Reads a file and returns all numbers in file as separated by commas

    Example input:

    1
    2
    3

    4

    5
    6

    Example output:

    [[1, 2. 3], [4]. [5, 6]]
    """
    lines = read_input_lines(filename, True)
    split_lines = []
    temp = []
    for line in lines:
        if line != "":
            temp.append(int(line))
        else:
            split_lines.append(temp)
            temp = []
    if temp != []:
        split_lines.append(temp)
    return split_lines


def read_input_int_matrix(filename: str) -> List[List[int]]:
    """
    Reads a file and returns all numbers in file as if it was a matrix

    :param filename:
    :return: "Matrix" (List[List[int]]) of input

    Input example:

    123
    456
    789

    Output example:

    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    """
    lines = read_input_lines(filename, strip_whitespace=True)
    matrix = []

    for line in lines:
        matrix.append([int(number) for number in line])

    return matrix


def split_list_on_entry(entries: List, signifier):
    split_list = []
    temp = []
    for entry in entries:
        if entry != signifier:
            temp.append(entry)
        else:
            split_list.append(temp)
            temp = []

    if temp != []:
        split_list.append(temp)

    return split_list


def add_pos(a, b):
    return a[0] + b[0], a[1] + b[1]


def print_matrix(matrix):
    for line in matrix:
        print(line)