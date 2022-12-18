import queue
from maze_func import print_maze, find_start


def find_path(
    maze: list[list[str]],
    stdscr,
    start: str,
    end: str,
    old_path=None,
    print_path: bool = False,
) -> tuple[list[tuple[int, int]], int]:
    if old_path is None:
        old_path = []

    start_pos = find_start(maze, start)

    visited_nodes_count = 0

    q = queue.LifoQueue()
    q.put((start_pos, [start_pos]))
    visited = set()

    while not q.empty():
        visited_nodes_count += 1
        current_pos, path = q.get()
        row, col = current_pos

        if current_pos in visited:
            continue
        visited.add(current_pos)

        stdscr.clear()
        if print_path:
            print_maze(maze, stdscr, old_path, path)
        stdscr.refresh()

        if maze[row][col] == end:
            return path, visited_nodes_count

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue

            r, c = neighbor
            if maze[r][c] == "#" or maze[r][c] == "/":
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))


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
