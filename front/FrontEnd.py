import curses
import curses.textpad

import sys

from CLIexceptions.CLI_Audio_Exception import CLI_Audio_File_Exception
from CLIexceptions.CLI_Audio_Exception import CLI_Audio_Screen_Size_Exception

import os
from os import listdir

class FrontEnd:

    #Class constructor. Takes Self and Player as parameters
    def __init__(self, player):
        self.player = player
        self.player.play("./media/music1.wav")
        curses.wrapper(self.menu)

    #Creates the menu for the GUI. Adds Functionality for buttons used in the menu.
    #Takes Self and Args as parameters
    def menu(self, args):
        self.stdscr = curses.initscr()
        self.stdscr.border()
        #checks with height and width of the current window. If height or width is too small. CLI_Audio_Screen_Size_Exception is thrown
        ##https://askubuntu.com/questions/98181/how-to-get-screen-size-through-python-curses
        height,width = self.stdscr.getmaxyx()
        if (height<20):
            raise CLI_Audio_Screen_Size_Exception("Screen size is too small. Increase the height of the screen to continue")
        if (width<90):
            raise CLI_Audio_Scr
        self.stdscr.addstr(0,0, "cli-audio",curses.A_REVERSE)
        self.stdscr.addstr(5,45, "c - Change current song")
        self.stdscr.addstr(6,45, "p - Play/Pause")
        self.stdscr.addstr(7,45, "l - Play library on playlist")
        self.stdscr.addstr(9,45, "ESC - Quit")

        lib = "./media"
        liblist = os.listdir(lib)
        y = 6
        for mus in liblist:
            self.stdscr.addstr(y,10,mus)
            y = y+1
        self.stdscr.addstr(5,10,"Files currently in library:")

        self.updateSong()
        self.stdscr.refresh()
        while True:
            #gets user input
            c = self.stdscr.getch()
            #used to escape or quit the current window
            if c == 27:
                self.quit()
            #used to pause the song
            elif c == ord('p'):
                self.player.pause()
            #used to change the song
            elif c == ord('c'):
                self.changeSong()
                self.updateSong()
                self.stdscr.touchwin()
                self.stdscr.refresh()
            #used to update the play playlist
            elif c == ord('l'):
                for mus in liblist:
                    self.player.stop()
                    self.player.play("./media/" + mus)
                    updateSong()
                    self.stdscr.touchwin()
                    self.stdscr.refresh()
                    while self.player.stream.output:
                        listen = True

    #Displays current playing song information. Used to update the song information
    def updateSong(self):
        self.stdscr.addstr(15,45, "                                            ")
        self.stdscr.addstr(15,45, "Now playing: " + self.player.getCurrentSong())

    #Provides the user with the ability to change the current song that is being played. User can select any song from the library
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
        exists = 0
        for f in liblist:
            if (f==path): 
                   exists = exists + 1
        if exists == 0:
            raise CLI_Audio_File_Exception("The file can not be played for some reason.")	
        self.player.stop()
        self.player.play("./media/" + path.decode(encoding="utf-8"))
        
    #used to quit or escape the player
    def quit(self):
        self.player.stop()
        exit()
