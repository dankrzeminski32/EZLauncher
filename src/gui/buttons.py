import tkinter as tk

def verify_game_pick(game_name):
    msg_box = tk.messagebox.askquestion('Start' + game_name, 'Are you sure you want to play ' + game_name, icon='warning')

    if msg_box == 'yes':
        #boot method for game
