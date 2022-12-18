def menu2():
    print("\nWybierz algorytm do wyznaczenia trasy zakupów:")
    print("[1] DFS")
    print("[2] Dijkstra")
    print("[3] A*")
    print("[0] Zakończ program")


def algorithm_selection():
    menu2()
    option = int(input("Wprowadź swój wybór: "))

    while option != 0:
        if option == 1:
            print("DFS")
            # ALGORITH_TO_RUN = dfs
            # main(stdscr)
            # TODO 1.Usunąć printy, 2.Dodać funkcjonalność programu: Przypisane algorytmu, i całą funkcjonalność
            break
        elif option == 2:
            print("Dijkstra")
            # ALGORITH_TO_RUN = dijkstra
            # main(stdscr)
            break
        elif option == 3:
            print("A*")
            # ALGORITH_TO_RUN = astar
            # main(stdscr)
            break
        else:
            print("Invalid option.\n")

        menu2()
        option = int(input("Enter your option: "))


def menu():
    # print("Wybierz sklep:\n[1] Biedronka\n[2] Lidl\n[3] Auchan\n")
    print("Wybierz sklep, w którym chcesz zrobić zakupy:")
    print("[1] Biedronka")
    print("[2] Lidl")
    print("[3] Auchan")
    print("[0] Zakończ program")


menu()
option = int(input("Wprowadź swój wybór: "))

# Domyślne ustawienia algorytmu i sklepu, które zostaną nadpisane?
# ALGORITH_TO_RUN = dijkstra
# base_maze = base_maze1

while option != 0:
    if option == 1:
        print("Biedronka")
        # base_maze = base_maze1
        # TODO 1.Usunąć printy, 2.Ustawienie odpowiedniego maze
        algorithm_selection()
        break
    elif option == 2:
        print("Lidl")
        # base_maze = base_maze2
        algorithm_selection()
        break
    elif option == 3:
        print("Auchan")
        # base_maze = base_maze3
        algorithm_selection()
        break
    else:
        print("Invalid option.\n")

    menu()
    option = int(input("Enter your option: "))

print("\nKoniec programu")
