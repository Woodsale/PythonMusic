import curses
import curses.textpad

import sys

from CLIexceptions.CLI_Audio_Exception import CLI_Audio_File_Exception
from CLIexceptions.CLI_Audio_Exception import CLI_Audio_Screen_Size_Exception

import os
from os import listdir

class FrontEnd:

    def __init__(self, player):
        self.player = player
        curses.wrapper(self.menu)

    def menu(self, args):
        self.stdscr = curses.initscr()
        self.stdscr.border()
        self.stdscr.addstr(0,0, "cli-audio",curses.A_REVERSE)
        self.stdscr.addstr(5,45, "c - Change current song")
        self.stdscr.addstr(6,45, "p - Play/Pause")
        self.stdscr.addstr(7,45, "l - Play library on playlist")
        self.stdscr.addstr(9,45, "ESC - Quit")

        lib = "/home/pydynn/343/PythonMusic/library"
        liblist = os.listdir(lib)
        y = 6
        for mus in liblist:
            self.stdscr.addstr(y,10,mus)
            y = y+1
        self.stdscr.addstr(5,10,"Files currently in library:")

        self.updateSong()
        self.stdscr.refresh()
        while True:
            c = self.stdscr.getch()
            if c == 27:
                self.quit()
            elif c == ord('p'):
                self.player.pause()
            elif c == ord('c'):
                self.changeSong()
                self.updateSong()
                self.stdscr.touchwin()
                self.stdscr.refresh()
            elif c == ord('l'):
                self.updateSong()
                 
    def updateSong(self):
        self.stdscr.addstr(15,45, "                                        ")
        self.stdscr.addstr(15,45, "Now playing: " + self.player.getCurrentSong())

    def changeSong(self):
        changeWindow = curses.newwin(5, 40, 5, 50)
        changeWindow.border()
        changeWindow.addstr(0,0, "What is the song's file name?", curses.A_REVERSE)
        self.stdscr.refresh()
        curses.echo()
        path = changeWindow.getstr(1,1, 30)
        curses.noecho()
        del changeWindow
        self.stdscr.touchwin()
        self.stdscr.refresh()
        self.player.stop()
        self.player.play(path.decode(encoding="utf-8"))
        

    def quit(self):
        self.player.stop()
        exit()
