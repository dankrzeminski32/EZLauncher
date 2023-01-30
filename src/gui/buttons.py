import tkinter as tk
from tkinter.messagebox import askyesno

def verify_game_pick(game_name):
    answer = answer = askyesno(title='Launch' + game_name + '?',message='Are you sure you want to launch ' + game_name + "?")

    if answer:
        #boot method for game
