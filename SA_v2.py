import astar
#import maze_func
import random
import math
import curses
# stdscr = curses.initscr()
from string import ascii_letters
from tqdm import tqdm
import time

import numpy as np

def letter_to_index(letter, random_items_amt):
    if letter == '}':
        return 0
    elif letter == '{':
        return random_items_amt + 1
    else:
        return ord(letter) - ord('a') + 1

def SA_v2(stdscr, maze, random_items_amt):

    start_time = time.time()

    #inicjalizacja zmiennych wejsciowych
    T = 1000
    T_min = 0.1
    alpha = 0.99
    iter = 100
    #temp_maze = chosen_maze

    # check = maze_func.check_if_checkpoints_in_maze(maze)
    # if check:
    #     letters = [letter for i, letter in enumerate(ascii_letters) if i < random_items_amt]
    #     #letters = ["}", *letters, "{"]

    letters = [letter for i, letter in enumerate(ascii_letters) if i < random_items_amt]
    letters = ["}", *letters, "{"]

    print("ścieżka początkowa:\n", letters,'\n')

    Path_Distance = np.zeros(shape=(len(letters), len(letters)))
    path = []
    for i in range(0, len(letters)):
        for j in range(0, len(letters)):
            if i == j:
                Path_Distance[i][j] = 0
            else:
                path_temp, visited_nodes_count_temp = astar.find_path(maze, stdscr, letters[i], letters[j], path, print_path=False)
                Path_Distance[i][j] = (len(path_temp))

    print('\n'"Macierz odleglosci miedzy punktami:"'\n', Path_Distance, '\n')

    #TODO - dodać nadpisywanie na ekranie poprawy wyników i czas działania programu
    while T > T_min:
        for i in range(0, iter-1):
            a = random.randint(1, len(letters)-2)
            b = random.randint(1, len(letters)-2)
            while a == b:
                b = random.randint(1, len(letters)-2)
            a, b = (a, b) if a < b else (b,a)


            #path_1 -> sciezka z letters[a] do letters[b]
            path_1 = Path_Distance[letter_to_index(letters[a], random_items_amt)][letter_to_index(letters[b], random_items_amt)]
            # if b == len(letters)-2:
            #     path_2 = 0
            # else:
                #path_2 -> letters[a+1], letters[b+1]
            path_2 = Path_Distance[letter_to_index(letters[a+1], random_items_amt)][letter_to_index(letters[b+1], random_items_amt)]
            #path_3 -> letters[a], letters[a+1]
            path_3 = Path_Distance[letter_to_index(letters[a], random_items_amt)][letter_to_index(letters[a+1], random_items_amt)]
            # if b == len(letters)-2:
            #     path_4 = 0
            # else:
                #path_4 -> letters[b], letters[b+1]
            path_4 = Path_Distance[letter_to_index(letters[b], random_items_amt)][letter_to_index(letters[b+1], random_items_amt)]

            delta = path_1 + path_2 - path_3 - path_4

            x = random.random()
            threshold = math.exp(-delta / T)

            if delta < 0 or threshold > x:
                #zamiana kolejności produktów w trasie
                letters[a+1:b+1] = letters[a+1:b+1][::-1]
            else:
                letters = letters

        T = alpha * T

    # for i in letters:
    #     final_path += Path_Distance[][]
    #     enumerate(ascii_letters)

    i = 0
    total_visited_count = 0
    path = []
    #letters = ["}", *letters, "{"]
    print("ścieżka koncowa:\n", letters,'\n')

    while i != len(letters) - 1:
        inter_path, visited_count = astar.find_path(maze, stdscr, letters[i], letters[i + 1], path, print_path=True)
        path.extend(inter_path)
        total_visited_count += visited_count
        i += 1

    end_time = time.time()

    print(
            f"\nIlosc krokow koniecznych do zebrania wszystkich zakupow to {len(path)} krokow,"
            f" gdzie jeden znak w przedstawionej wczesniej symulacji to jeden krok."
        )
    print(f"Ilosc wszystkich sprawdzonych krokow to {total_visited_count}")

    elapsed_time = end_time - start_time
    print('Execution time:', elapsed_time, 'seconds')
