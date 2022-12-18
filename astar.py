#import queue
from math import sqrt
from queue import PriorityQueue
from dataclasses import dataclass, field
from typing import Any

from maze_func import print_maze, find_start


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: Any=field(compare=False)


def distance(start: tuple[int, int], end: tuple[int, int], current: tuple[int, int]) -> float:
    distance_start = sqrt((current[0] - start[0]) ** 2 + (current[1] - start[1]) ** 2)
    distance_end = sqrt((current[0] - end[0]) ** 2 + (current[1] - end[1]) ** 2)
    return distance_start + distance_end


def find_path(maze: list[list[str]], stdscr, start: str, end: str, old_path=None, print_path: bool = False) -> tuple[list[
    tuple[int, int]], int]:
    if old_path is None:
        old_path = []

    visited_nodes_count = 0

    start_pos = find_start(maze, start)
    end_pos = find_start(maze, end)

    q = PriorityQueue()

    q.put(PrioritizedItem(0, (start_pos, [start_pos])))
    visited = set()

    while not q.empty():
        visited_nodes_count += 1
        current_pos, path = q.get().item
        row, col = current_pos

        stdscr.clear()
        if print_path:
            print_maze(maze, stdscr, old_path, path)
        stdscr.refresh()

        if current_pos == end_pos:
            return path, visited_nodes_count

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == "#" or maze[r][c] == "/":
                continue

            new_path = path + [neighbor]
            q.put(PrioritizedItem(distance(start_pos, end_pos, current_pos), (neighbor, new_path)))
            visited.add(neighbor)


def find_neighbors(maze: list[list[str]], row: int, col: int) -> list[tuple[int, int]]:
    neighbors = []

    if row > 0:  # UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  # DOWN
        neighbors.append((row + 1, col))
    if col > 0:  # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):  # RIGHT
        neighbors.append((row, col + 1))

    return neighbors