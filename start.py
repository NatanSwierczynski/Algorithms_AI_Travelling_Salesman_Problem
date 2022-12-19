#import curses
#stdscr = curses.initscr()
from menu import menu_sa

chosen_maze, algorithm_choice, random_items_amt = menu_sa()
#print(chosen_maze, algorithm_choice, random_items_amt)
