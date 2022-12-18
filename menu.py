from mazes import base_maze, base_maze1, base_maze2
import dijkstra
import astar
import dfs
from run import run

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
]


def menu():
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
