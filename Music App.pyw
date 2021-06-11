import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory  # filedialog from tkinter has open and save dialog fiunctions
# askdirectory from filedialog presents user with pop up to choose directory
import os  # os module helps to for interacting with operating system..

musicplayer = tkr.Tk()
musicplayer.title("Music Player")
musicplayer.geometry("450x350")

directory = askdirectory()
os.chdir(directory)  # os.chdir() change the current working directory to specified path
songlist = os.listdir()  # os.listdir() returns a list containing the name of entries in the directory given by path
playlist = tkr.Listbox(musicplayer, font="Helvetica 12 bold", bg="light blue",
                       selectmode=tkr.SINGLE)  # listbox() contains the songs list
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos += 1

pygame.init()
pygame.mixer.init()


def play():
    pygame.mixer.music.load(
        playlist.get(tkr.ACTIVE))  ##active refers tha=e active file that is actually selected hen mouse move over it
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()


def ExitMusicPlayer():
    pygame.mixer.music.stop()


def pause():
    pygame.mixer.music.pause()


def unpause():
    pygame.mixer.music.unpause()


Button1 = tkr.Button(musicplayer, width=5, height=3, font="Helvatica 12 bold", text="PLAY", command=play, bg="red",
                     fg="white")
Button2 = tkr.Button(musicplayer, width=5, height=3, font="Helvatica 12 bold", text="STOP", command=ExitMusicPlayer,
                     bg="light green", fg="white")
Button3 = tkr.Button(musicplayer, width=5, height=3, font="Helvatica 12 bold", text="PAUSE", command=pause, bg="purple",
                     fg="white")
Button4 = tkr.Button(musicplayer, width=5, height=3, font="Helvatica 12 bold", text="UNPAUSE", command=unpause,
                     bg="green", fg="white")

var = tkr.StringVar()
songtitle = tkr.Label(musicplayer, font="Helvetica 12 bold", textvariable=var)

songtitle.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")
playlist.pack(fill="both", expand="yes")

musicplayer.mainloop()
