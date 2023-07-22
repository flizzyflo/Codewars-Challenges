"""
Kate constantly finds herself in some kind of a maze. Help her to find a way out!.

For a given maze and Kate's position find if there is a way out. Your function should return True or False.

Each maze is defined as a list of strings, where each char stays for a single maze "cell". ' ' (space) can be stepped on, '#' means wall and 'k' stays for Kate's starting position. Note that the maze may not always be square or even rectangular.

Kate can move left, up, right or down only.

There should be only one Kate in a maze. In any other case you have to throw an exception.
Example input

['# ##',
 '# k#',
 '####']

Example output

True
Example input

['####'.
 '# k#',
 '####']

Example output

False

"""
from queue import Queue


def get_starting_point_for(name: str, maze) -> tuple[int, int]:
    row, col = [(idx, l.find(name)) for idx, l in enumerate(maze) if l.find("k") != -1][0]
    return row, col


def is_wall(value: str, wall: str = "#") -> bool:
    return value == wall


def is_valid_exit(position: tuple[int, int], maze: list[str]) -> bool:
    row, col = position
    position_type = maze[row][col]
    is_possible_way = position_type == " "
    return ((row == len(maze) - 1 or row == 0) or (col == len(maze[0]) - 1 or col == 0)) and is_possible_way


def row_is_in_bounds(position: int, maze: list[str]) -> bool:
    return 0 <= position < len(maze)


def col_is_in_bounds(position: int, maze: list[str]) -> bool:
    return 0 <= position < len(maze[0])


def has_exit(maze: list[str]) -> bool:

    if len(maze) == 1 and "k" in maze[0]:
        return True

    row, col = get_starting_point_for(name="k", maze=maze)
    next_steps: Queue[tuple[int, int]] = Queue()
    next_steps.put((row, col))
    visited_spots: set[tuple[int, int]] = set()
    visited_spots.add((row, col))

    adventurer_counter = sum(row.count("k") for row in maze)
    if adventurer_counter > 1:
        raise Exception("There should not be more Kates than one")

    while not next_steps.empty():
        row, col = next_steps.get()
        visited_spots.add((row, col))

        if is_valid_exit((row, col), maze):
            return True

        if not row_is_in_bounds(row + 1, maze) or not row_is_in_bounds(row - 1, maze):
            continue

        if not col_is_in_bounds(col + 1, maze) or not col_is_in_bounds(col - 1, maze):
            continue

        if not is_wall(maze[row + 1][col]) and (row + 1, col) not in visited_spots:
            next_steps.put((row + 1, col))
        if not is_wall(maze[row - 1][col]) and (row - 1, col) not in visited_spots:
            next_steps.put((row - 1, col))
        if not is_wall(maze[row][col + 1]) and (row, col + 1) not in visited_spots:
            next_steps.put((row, col + 1))
        if not is_wall(maze[row][col - 1]) and (row, col - 1) not in visited_spots:
            next_steps.put((row, col - 1))

    return False
