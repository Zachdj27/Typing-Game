import curses
def main(stdscr):
    menu = ["Start Game","Exit"]
    
    def print_menu(stdscr, selected):
        '''Prints home_screen'''
        stdscr.clear()
        height, width = stdscr.getmaaxy()
        for idx, row in enumerate(menu):
            x = width // 2 - len(row) // 2
            y = height // 2 - len(row) // 2
            if idx == selected:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(y, x , row)
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.attroff(curses.A_REVERSE)
        stdscr.noutrefresh()
                
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
            elif key == curses.KEY_DOWN and row < 1:
                row += 1
            elif key == curses.KEY_ENTER or key in [10,13]:
                if row == 0:
                    typing_game()
                elif row == 1:
                    break
        print_menu(stdscr, row)

                    
    
    home_screen()