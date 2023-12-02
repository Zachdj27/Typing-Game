import curses
def main(stdscr):
    menu = ["Start Game","Exit"]
    
    def print_menu(stdscr):
        '''Prints home_screen'''
        pass
    
    def typing_game(stdscr):
        '''Plays game'''
        pass

    def home_screen():
        '''Lets user choose option in home screen'''
        row = 0
        while True:
            key = stdscr.getch()
            if key == curses.KEY_UP and row > 0:
                row -= 1
            elif key == curses.KEY_DOWN and row < len(menu) - 1:
                row += 1
            elif key == curses.KEY_ENTER or key in [10,13]:
                if row == 0:
                    typing_game()
                elif row == 1:
                    break
            print_menu(stdscr, row)

                    
    
    home_screen()