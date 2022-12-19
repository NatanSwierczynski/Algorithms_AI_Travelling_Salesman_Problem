from string import ascii_letters
from mazes import base_maze, base_maze1, base_maze2
import curses
import maze_func

# Poniższa zmienna decyduje czy należy wykreślić śnieżkę końcową w terminalu
PRINT_PATH = False
# Showcase rozumiemy jako przedstawienie w terminalu kolejności wykonywania działań algorytmu
SHOWCASE = True


def run(stdscr, chosen_maze, algorithm, algo_name, amt_random_items) -> None:
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
            inter_path, visited_count = algorithm.find_path(
                chosen_maze,
                stdscr,
                letters[i],
                letters[i + 1],
                path,
                print_path=SHOWCASE,
            )
            path.extend(inter_path)
            total_visited_count += visited_count
            # path.extend(algorithm.find_path(chosen_maze, stdscr, letters[i], letters[i+1], path, print_path=SHOWCASE))
            i += 1
    else:
        path, total_visited_count = algorithm.find_path(
            chosen_maze, stdscr, "}", "{", path, print_path=SHOWCASE
        )
        # path.extend(algorithm.find_path(chosen_maze, stdscr, "}", "{", path, print_path=SHOWCASE))
    if PRINT_PATH:
        maze_func.print_maze(chosen_maze, stdscr, path, path)

    print(
        f"\n{algo_name}: Ilosc krokow koniecznych do zebrania wszystkich zakupow to {len(path)} krokow, gdzie jeden znak w przedstawionej wczesniej symulacji to jeden krok."
    )
    print(f"Ilosc wszystkich sprawdzonych krokow to {total_visited_count}")
    # print(f"{coords}")
    if PRINT_PATH or SHOWCASE:
        stdscr.getch()

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