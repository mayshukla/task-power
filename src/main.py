# standard python modules
import curses
from curses.textpad import Textbox, rectangle

# my modules
from datetools import convert_weekday_to_string
from Task import Task

def main(stdscr):
    #stdscr.clear()
    #curses.curs_set(False) #turn off visible cursor

    stdscr.addstr('Welcome to Task Power!')

    #create a new window and a text input box inside it
    editwin = curses.newwin(1,20, 3,1)
    rectangle(stdscr, 2,0, 1+2+1,1+20+1)
    stdscr.refresh()

    box = Textbox(editwin)
    
    #let the user edit unit Ctrl-G struck
    box.edit()

    #get the input
    input_text = box.gather()

    #spit back the input to the second line of stdscr
    stdscr.addstr(1, 0, input_text)
    stdscr.refresh()

    #create a new window and a text input box inside it
    editwin2 = curses.newwin(1,20, 6,1)
    
    #border() doesn't see to work
    #editwin2.border([0[, 0[, 0[, 0[, 0[, 0[, 0[, 0]]]]]]]])
    rectangle(stdscr, 5,0, 1+5+1,1+20+1)
    stdscr.refresh()

    box2 = Textbox(editwin2)
    box2.edit()
    input_text2 = box2.gather()

    stdscr.addstr(1, 23, input_text2)
    stdscr.refresh()

    #try going back and editing first window
    box.edit()

    stdscr.getkey() #wait for any keypress

# initialize curses stdscr object and call main function
curses.wrapper(main)
print('curses closed')
