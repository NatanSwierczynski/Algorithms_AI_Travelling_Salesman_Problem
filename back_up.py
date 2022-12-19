import main


def simulated_annealing():

    #T, Tmax, Tmin
    #max_iter, max_iter_per_epoch

    #randomize_items_in_store(...) -> maze (mamy maze z losowymi punktami)

    #initial_temp = 1000
    #alpha = 0.99
    #current_temp = initial_temp

    # T_max = 100
    # T_min = 0.1

    Licznik = 1000  #max_iter
    i = 0

    while Licznik > 1:

        Best_path = 0



''' Obliczanie długości ścieżki dla danego ułożenia produktów '''

from string import ascii_letters
import maze_func


def run_sa(stdscr, chosen_maze, algorithm, amt_random_items) -> None:
    path = []
    total_visited_count = 0
    check = maze_func.check_if_checkpoints_in_maze(chosen_maze)
    if check:
        letters = [
            letter for i, letter in enumerate(ascii_letters) if i < amt_random_items
        ]
        letters = ["}", *letters, "{"]
        i = 0
        while i != len(letters) - 1:
            inter_path, visited_count = algorithm.find_path(chosen_maze, stdscr, letters[i], letters[i + 1], path, print_path=False)
            path.extend(inter_path)
            total_visited_count += visited_count
            i += 1
    else:
        path, total_visited_count = algorithm.find_path(
            chosen_maze, stdscr, "}", "{", path, print_path=False
        )

    temp_path = len(path)
    return temp_path
    #return temp_path, total_visited_count


''' Obliczanie długości ścieżki między dwoma punktami '''
'''
def tour_sa(stdscr, chosen_maze, algorithm, amt_random_items, a, b) -> None:
    path = []
    total_visited_count = 0
    check = maze_func.check_if_checkpoints_in_maze(chosen_maze)
    if check:
        letters = [
            letter for i, letter in enumerate(ascii_letters) if i < amt_random_items
        ]
        letters = ["}", *letters, "{"]
        i = 0
        while i != len(letters) - 1:
            inter_path, visited_count = algorithm.find_path(chosen_maze, stdscr, letters[i], letters[i + 1], path, print_path=False)
            path.extend(inter_path)
            total_visited_count += visited_count
            i += 1
    else:
        path, total_visited_count = algorithm.find_path(
            chosen_maze, stdscr, "}", "{", path, print_path=False
        )

    temp_path = len(path)
    return temp_path
    #return temp_path, total_visited_count
'''

''' Main -> bez sortowania kolejności produktów '''

import dfs
import astar
import dijkstra
from run import run
from menu import menu
import maze_func
import random
import math
import curses
stdscr = curses.initscr()

def main_sa(stdscr):
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)

chosen_maze, algorithm_choice, random_items_amt = menu()
maze = maze_func.randomize_items_in_store(chosen_maze, how_many_items=random_items_amt)

for algo in algorithm_choice:
    if algo == "1":
        maze = maze_func.order_random_items_to_start(maze, maze_func.get_checkpoint_coords(chosen_maze))
        run(stdscr, maze, dijkstra, "Dijkstra", random_items_amt)
    if algo == "2":
        maze = maze_func.order_random_items_to_start(maze, maze_func.get_checkpoint_coords(chosen_maze))
        run(stdscr, maze, astar, "A*", random_items_amt)
    if algo == "3":
        maze = maze_func.order_random_items_to_start(maze, maze_func.get_checkpoint_coords(chosen_maze))
        run(stdscr, maze, dfs, "DFS", random_items_amt)
    # Dodanie 4 opcji gdy wybrany jest SA -> uruchomienie run_sa dla A*
    if algo == "4":
        best_path = run_sa(stdscr, maze, astar, random_items_amt)

#Obliczenia całkowitej ścieżki dla losowego ułożenia produktów - losowe ułożenie ale i tak idzie alfabetycznie

#inicjalizacja zmiennych wejsciowych
T = 100
T_min = 0.1
alpha = 0.99
temp_maze = maze
#temp_maze = chosen_maze

check = maze_func.check_if_checkpoints_in_maze(temp_maze)
if check:
    letters = [letter for i, letter in enumerate(ascii_letters) if i < random_items_amt]
    #letters = ["}", *letters, "{"]

#TODO - Pętla while / for - dla

while T > T_min:
    #i = random.randint(1, random_items_amt + 1)
    a, b = random.sampe(letters, 2)
    #temp_letters = letters
    #temp_letters[min(a, b):max(a, b)] = letters[min(a, b):max(a, b)][::-1]

    #TODO - wyznaczyć scieżkę dla temp_letters
    '''
    path = []
    total_visited_count = 0
    i = 0
    while i != len(letters) - 1:
        inter_path, visited_count = astar.find_path(chosen_maze, stdscr, letters[i], letters[i + 1], path, print_path=False)
        path.extend(inter_path)
        total_visited_count += visited_count
        i += 1
    '''
    #temp_path = run_sa(stdscr, maze, astar, random_items_amt)

    #letters[a], letters[a+1], letters[b], letters[b+1]
    path = []
    path_1, visited_nodes_count_1 = astar.find_path(chosen_maze, stdscr, letters[a], letters[b], path, print_path=False)
    #path = []
    path_2, visited_nodes_count_2 = astar.find_path(chosen_maze, stdscr, letters[a+1], letters[b+1], path, print_path=False)
    #path = []
    path_3, visited_nodes_count_3 = astar.find_path(chosen_maze, stdscr, letters[a], letters[a+1], path, print_path=False)
    #path = []
    path_4, visited_nodes_count_4 = astar.find_path(chosen_maze, stdscr, letters[b], letters[b+1], path, print_path=False)

    delta = path_1 + path_2 - path_3 - path_4

    x = random.random()
    threshold = math.exp(-delta / T)

    if delta < 0 or  threshold > x:
        #zamiana kolejności produktów w trasie
        letters[min(a, b):max(a, b)] = letters[min(a, b):max(a, b)][::-1]
    else:
        letters = letters

    #TODO - nadpisywanie maze - poprzez zapisywanie letters do temp_maze

    T = alpha * T


curses.wrapper(main)


def inverse(letters):
    "Inverses the order of cities in a route between node one and node two"

    node_one = random.choice(letters)
    new_letters = list(filter(lambda product: product != node_one, letters))  # route without the selected node one
    node_two = random.choice(new_letters)
    letters[min(node_one, node_two):max(node_one, node_two)] = letters[min(node_one, node_two):max(node_one, node_two)][::-1]

    return letters





''' Menu -> przy wyborze SA, algorytm = A* '''

from mazes import base_maze, base_maze1, base_maze2

mazes = [base_maze, base_maze1, base_maze2]

algorithm_possibilities = [
    "1",
    "2",
    "3",
    "12",
    "21",
    "13",
    "31",
    "23",
    "32",
    "123",
    "132",
    "213",
    "231",
    "312",
    "321",
    "4",
]


def menu_sa():
    print(
        "Ta aplikacja ma za zadanie wyznaczyć najkrótsze trasy na terenie jednego z trzech dostępnych układów sklepów"
    )

    while True:
        print(
            "Proszę wybrać jeden z trzech dostępnych sklepów:\n1: Układ 1\n2: Układ 2\n3: Układ 3"
        )
        try:
            maze_choice = int(input("Wybór: "))
            if maze_choice in (1, 2, 3):
                break
        except ValueError:
            print("Proszę podać poprawną wartość")
            continue
    chosen_maze = mazes[maze_choice - 1]


    #Dodanie do menu opcji wyboru symulowanego wyżarzania
    while True:
        print(
            "\nCzy wykorzystać symulowane wyżarzanie do znalezienia trasy?\n1: TAK\n2: NIE"
        )
        try:
            sa_choice = int(input("Wybór: "))
            if sa_choice in (1, 2):
                break
        except ValueError:
            print("Proszę podać poprawną wartość")
            continue

        if sa_choice == 1:
            algorithm_choice = 4
        else:
            while True:
                print(
                    "\nProszę wybrać jakie algorytmy wykorzystać podczas symulacji:\n1: Dijkstra\n2: A*\n3: DFS"
                )
                print(
                    "Możliwe jest wybranie więcej niż jednego algorytmu, np: '123' - wybór wszystkich dostępnych algorytmów"
                )
                algorithm_choice = input("Wybór: ")
                if algorithm_choice in algorithm_possibilities:
                    break
                else:
                    print("Proszę podać poprawną odpowiedź")


    while True:
        print(
            "\nProszę określić jak wiele przedmiotów wygenerwować w danym sklepie (wartość od 0 do 25)."
        )
        try:
            random_items_amt = int(input("Ilość: "))
            if 0 <= random_items_amt <= 25:
                break
        except ValueError:
            print("Proszę podać poprawną wartość")
            continue

    return chosen_maze, algorithm_choice, random_items_amt