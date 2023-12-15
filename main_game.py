import curses
import requests
from curses import wrapper


menu = ["Play Typing Game", "Tell Me A Dad Joke", "Exit"] 

def fetch_joke():
    return requests.get("https://icanhazdadjoke.com/", headers={"Accept": "text/plain"}).content.decode('U8')

def print_menu(stdscr, selected):
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = width // 2 - len(row) // 2
        y = height // 2 - len(menu) // 2 + idx
        if idx == selected:
            stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(y, x , row)
            stdscr.attroff(curses.A_REVERSE)
        else:
            stdscr.addstr(y, x, row)
    stdscr.noutrefresh()
        
        
def make_me_laugh(stdscr):
    stdscr.clear()
    while True:
        #get rid of exceptions from huge texts
        try:
            setup = joke = fetch_joke()
            punchline = ""
            if "?" in joke:
                setup, punchline = [str(line) for line in joke.split("?")]
            
            height, width = stdscr.getmaxyx()
            x_setup = width // 2 - len(setup) // 2
            x_punchline = width // 2 - len(punchline) // 2
            y = height // 2
            stdscr.addstr(y, x_setup, setup + '?' * ('?' in joke))
            stdscr.addstr(y + 1, x_punchline, punchline)
            break
        except curses.error:
           continue
    stdscr.refresh()
    stdscr.getch()
           
def home_screen(stdscr):
        
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
                wpm_test(stdscr)
            if current_row == 1:
                make_me_laugh(stdscr)
            if current_row == 2:
                break
        print_menu(stdscr, current_row)
        curses.doupdate()    
    
def wpm_test(stdscr):
    target_text = "Hello world. This is some test text for this app!"
    current_text = []
    
    while True:
        stdscr.clear()
        stdscr.addstr(target_text)
        
        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1) )
        stdscr.refresh()
      
        key = stdscr.getkey()
        
        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        else:
            current_text.append(key)
        
        
def main(stdscr):
  curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
  home_screen(stdscr)



    
wrapper(main)