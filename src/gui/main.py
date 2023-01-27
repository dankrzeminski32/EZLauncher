import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

<<<<<<< HEAD:gui/main.py
root = customtkinter.CTk()
root.geometry("500x350")
root.title("EZLauncher")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

root.mainloop()
=======
def base():
    r = tk.Tk()
    r.title("EZLauncher")
    r.geometry("900x750")
    r.mainloop()
>>>>>>> 413000e480e19bb95c86f9c87657e84f181b5bdc:src/gui/main.py
