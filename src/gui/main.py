import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("EZLauncher")
        self.minsize(1200, 750)

        self.button = customtkinter.CTkButton(master=self, command=self.button_callback)
        self.button.pack(padx=20, pady=20)

    def button_callback(self):
        print("button pressed")


if __name__ == "__main__":
    app = App()
    app.mainloop()
