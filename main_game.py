import curses
from curses import wrapper


def print_menu(stdscr, selected):
    menu = ["Start Game","Tell me a Dad Joke!","Exit"]
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = width // 2 - len(row) // 2
        y = height // 2 - len(row) // 2
        if idx == selected:
            stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(y, x , row)
            stdscr.attroff(curses.A_REVERSE)
        else:
            stdscr.addstr(y, x, row)
        stdscr.noutrefresh()
        
        
def make_me_laugh(stdscr):
    pass
                
                
def typing_game(stdscr):
    pass
    
    
def update_home_screen():
    pass
        
        
def main(stdscr):
    
    def home_screen(stdscr):
        height, width = stdscr.getmaxyx()
        
        curses.curs_set(0)
        current_row = 0
        print_menu(stdscr, current_row)
        
        curses.doupdate()
        
        while True:
            key = stdscr.getch()
            if key == curses.KEY_UP and current_row > 0:
                current_row -= 1
            elif key == curses.KEY_DOWN and current_row < 2:
                current_row += 1
            elif key == curses.KEY_ENTER or key in [10,13]:
                if current_row == 0:
                    typing_game()
                if current_row == 1:
                    make_me_laugh(stdscr)
                if current_row == 2:
                    break
        print_menu(stdscr, current_row)

                    
    
    home_screen(stdscr)

    
wrapper(main)