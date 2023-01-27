import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("EZLauncher")
        self.minsize(1200, 750)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(
            self.navigation_frame,
            text="Launcher Hub",
            compound="left",
            font=customtkinter.CTkFont(size=15, weight="bold"),
        )

        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # To add button action add command= (method that launches the game)
        self.home_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Game Launch Test HERE",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
        )

        self.home_button.grid(row=1, column=0, sticky="ew")

    def button_callback(self):
        print("button pressed")


if __name__ == "__main__":
    app = App()
    app.mainloop()
