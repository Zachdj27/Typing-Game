import curses
import requests
import time
from curses import wrapper


menu = ["Play Typing Game", "Tell Me A Dad Joke", "Exit"] 

def fetch_joke():
    while True:
        joke = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "text/plain"}).content.decode('UTF-8')
        if "\n" in joke:
            continue
        else:
            return joke
                

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
       # i’m using try/except to get rid of exceptions from huge texts
       try:
           setup = joke = fetch_joke()
           punchline = ''
           if '?' in joke:
               setup, punchline = [str(line) for line in joke.split('?')]


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
                while(True):
                    height, width = stdscr.getmaxyx()
                    congrats = "Congrats on completing the text! Press any key to conitnue or press escape to quit."
                    x = width // 2 - len(congrats) // 2
                    y = height // 2
                    
                    stdscr.addstr(y - 3, x, congrats)
                    key = stdscr.getkey()
                    
                    if ord(key) == 27:
                        break
                    else:
                        wpm_test(stdscr)
                        
            if current_row == 1:
                make_me_laugh(stdscr)
            if current_row == 2:
                break
            
        print_menu(stdscr, current_row)
        curses.doupdate()    

def display_text(stdscr, target, current, wpm = 0):
        height, width = stdscr.getmaxyx()
        x = width // 2 - len(target) // 2
        y = height // 2
        stdscr.addstr(y , x, target)
        stdscr.addstr(y + 2, x, f"WPM: {wpm}")
        
        for i, char in enumerate(current):
            correct_char = target[i]
            color = curses.color_pair(1)
            if char != correct_char:
                color = curses.color_pair(2)
          
            stdscr.addstr(y, i + x, char, color)


def wpm_test(stdscr):
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)
    target = fetch_joke()
    
    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed/60)) / 5)
        
        stdscr.clear()
        display_text(stdscr, target, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target:
            stdscr.nodelay(False)
            break
        try:
            key = stdscr.getkey()
        except:
            continue
        
        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target):
            if key in ("KEY_ENTER","\n", "\r"):
                current_text.append("")
            else:
                current_text.append(key)
        
        
def main(stdscr):
  curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
  curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
  
  home_screen(stdscr)



    
wrapper(main)