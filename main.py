import curses
import dfs
import astar
import dijkstra
from mazes import base_maze, base_maze1, base_maze2
from run import run
from menu import menu
import maze_func


chosen_maze, algorithm_choice, random_items_amt = menu()
maze = maze_func.randomize_items_in_store(chosen_maze, how_many_items=random_items_amt)
maze = maze_func.order_random_items_to_start(
    chosen_maze, maze_func.get_checkpoint_coords(chosen_maze)
)

def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    for algo in algorithm_choice:
        if algo == "1":
            run(stdscr, maze, dijkstra, "Dijkstra", random_items_amt)
        if algo == "2":
            run(stdscr, maze, astar, "A*", random_items_amt)
        if algo == "3":
            run(stdscr, maze, dfs, "DFS", random_items_amt)

curses.wrapper(main)
