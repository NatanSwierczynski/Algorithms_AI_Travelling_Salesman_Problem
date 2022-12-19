import astar
#import maze_func
import random
import math
import curses
# stdscr = curses.initscr()
from string import ascii_letters
from tqdm import tqdm


def SA(stdscr, maze, random_items_amt):
    #inicjalizacja zmiennych wejsciowych
    T = 100
    T_min = 0.1
    alpha = 0.99
    #temp_maze = chosen_maze

    # check = maze_func.check_if_checkpoints_in_maze(maze)
    # if check:
    #     letters = [letter for i, letter in enumerate(ascii_letters) if i < random_items_amt]
    #     #letters = ["}", *letters, "{"]

    letters = [letter for i, letter in enumerate(ascii_letters) if i < random_items_amt]

    # progress = tqdm()

    # stdscr.clear()
    # iter_count = 0
    while T > T_min:
        # iter_count += 1
        # stdscr.addstr(0, 0, f'{iter_count} iterations')
        # stdscr.refresh()
        # progress.update()
        #a, b = random.sample(letters, 2)
        a = random.randint(0, len(letters)-1)
        b = random.randint(0, len(letters)-1)
        while a == b:
            b = random.randint(0, len(letters)-1)
        a, b = (a, b) if a < b else (b,a)

        path = []
        path_1, visited_nodes_count_1 = astar.find_path(maze, stdscr, letters[a], letters[b], path, print_path=False)
        #path = []
        if b == len(letters)-1:
            path_2 = []
        else:
            path_2, visited_nodes_count_2 = astar.find_path(maze, stdscr, letters[a+1], letters[b+1], path, print_path=False)
        #path = []
        path_3, visited_nodes_count_3 = astar.find_path(maze, stdscr, letters[a], letters[a+1], path, print_path=False)
        #path = []
        if b == len(letters)-1:
            path_4 = []
        else:
            path_4, visited_nodes_count_4 = astar.find_path(maze, stdscr, letters[b], letters[b+1], path, print_path=False)

        delta = len(path_1) + len(path_2) - len(path_3) - len(path_4)

        x = random.random()
        threshold = math.exp(-delta / T)

        if delta < 0 or threshold > x:
            #zamiana kolejności produktów w trasie
            letters[min(a, b):max(a, b)] = letters[min(a, b):max(a, b)][::-1]
        else:
            letters = letters

        #TODO - nadpisywanie maze - poprzez zapisywanie letters do temp_maze

        T = alpha * T

    # progress.close()

    i = 0
    total_visited_count = 0
    path = []
    while i != len(letters) - 1:
        inter_path, visited_count = astar.find_path(maze, stdscr, letters[i], letters[i + 1], path, print_path=True)
        path.extend(inter_path)
        total_visited_count += visited_count
        i += 1

    print(
            f"\n Ilosc krokow koniecznych do zebrania wszystkich zakupow to {len(path)} krokow,"
            f" gdzie jeden znak w przedstawionej wczesniej symulacji to jeden krok."
        )
    print(f"Ilosc wszystkich sprawdzonych krokow to {total_visited_count}")
