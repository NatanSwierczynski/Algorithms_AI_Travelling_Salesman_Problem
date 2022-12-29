import curses
import random
from string import ascii_letters
from numpy import sqrt


def print_maze(
    maze: list[list[str]], stdscr, old_path: list[tuple[int, int]], path=None
) -> None:
    if path is None:
        path = []
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2)
    YELLOW = curses.color_pair(3)
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                try:
                    stdscr.addstr(i, j * 2, "@", YELLOW)
                except curses.error:
                    pass
            elif (i, j) in old_path:
                try:
                    stdscr.addstr(i, j * 2, "@", RED)
                except curses.error:
                    pass
            else:
                try:
                    stdscr.addstr(i, j * 2, value, BLUE)
                except curses.error:
                    pass


def find_start(maze: list[list[str]], start: str) -> tuple[int, int] | None:
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return (i, j)

    return None


def flatten_the_maze(maze: list[list[str]]) -> list[str]:
    return [item for sublist in maze for item in sublist]


def get_checkpoint_coords(maze: list[list[str]]) -> list[tuple[int, int]] | None:
    coords = []
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value in ascii_letters:
                coords.append((i, j))
    return coords


def check_if_checkpoints_in_maze(maze: list[list[str]]) -> list[int] | None:
    flat_maze = flatten_the_maze(maze)
    numbers_in_maze = []
    for character in flat_maze:
        if character.isalpha():
            numbers_in_maze.append(character)
    if not numbers_in_maze:
        return []
    return max(numbers_in_maze)


def randomize_items_in_store(
    maze: list[list[str]], how_many_items: int
) -> list[list[str]]:
    i = 0
    if how_many_items <= 0:
        return maze
    while True:
        for x, column in enumerate(maze):
            for y, character in enumerate(column):
                if i >= how_many_items:
                    return maze
                if character == "#" and random.randint(0,100) > 95: #(0, 10) > 8:
                    maze[x][y] = ascii_letters[i]
                    i += 1


def order_random_items_to_start(
    maze: list[list[str]], coords: list[tuple[int, int]]
) -> list[list[str]]:
    start_coord = find_start(maze, start="}")
    distances = [
        sqrt((start_coord[0] - a) ** 2 + (start_coord[1] - b) ** 2) for a, b in coords
        #((abs(start_coord[0] - a)) + abs(start_coord[1] - b)) for a, b in coords
    ]
    dictionary = {coord: distance for coord, distance in zip(coords, distances)}
    sorted_keys = sorted(dictionary, key=dictionary.get)
    sorted_dict = {}
    for k in sorted_keys:
        sorted_dict[k] = dictionary[k]
    new_coords = [key for key in sorted_dict.keys()]

    i = 0
    for coord in new_coords:
        maze[coord[0]][coord[1]] = ascii_letters[i]
        i += 1
    return maze

