from SA import SA
from SA_v2 import SA_v2
import dfs
import astar
import dijkstra
from run import run
# from run import run_sa
# from menu import menu
from menu import menu_sa
import maze_func
import curses
import random

#stdscr = curses.initscr()

chosen_maze, algorithm_choice, random_items_amt = menu_sa()
random.seed(10)
initial_maze = maze_func.randomize_items_in_store(chosen_maze, how_many_items=random_items_amt)
random.seed()
maze_0 = maze_func.order_random_items_to_start(initial_maze, maze_func.get_checkpoint_coords(chosen_maze))


def main_sa(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    for algo in algorithm_choice:
        if algo == "1":
            # algo_name = "Dijkstra"
            run(stdscr, maze_0, dijkstra, "Dijkstra", random_items_amt)
        if algo == "2":
            # algo_name = "A*"
            run(stdscr, maze_0, astar, "A*", random_items_amt)
        if algo == "3":
            # algo_name = "DFS"
            run(stdscr, maze_0, dfs, "DFS", random_items_amt)
        # Dodanie 4 opcji gdy wybrany jest SA -> uruchomienie run_sa dla A*
        if algo == "4":
            # algo_name = "SA with A*"
            # best_path = run_sa(stdscr, maze, astar, random_items_amt)
            # SA(stdscr, initial_maze, random_items_amt)
            SA_v2(stdscr, initial_maze, random_items_amt)


curses.wrapper(main_sa)
