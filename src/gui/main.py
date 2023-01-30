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
        self.navigation_frame.grid_rowconfigure(6, weight=1)

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
            command=self.home_button_event,
        )

        self.home_button.grid(row=1, column=0, sticky="ew")

        self.steam_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Steam",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
        )
        self.steam_button.grid(row=2, column=0, sticky="ew")

        self.battle_net_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Battle.net",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
        )
        self.battle_net_button.grid(row=3, column=0, sticky="ew")

        self.epic_games_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Epic Games",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
        )
        self.epic_games_button.grid(row=4, column=0, sticky="ew")

        self.ubisoft_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="Ubisoft",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
        )
        self.ubisoft_button.grid(row=4, column=0, sticky="ew")

        self.home_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent"
        )
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="")
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_button_2 = customtkinter.CTkButton(
            self.home_frame,
            text="CTkButton",
            compound="right",
        )
        self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.home_frame_button_3 = customtkinter.CTkButton(
            self.home_frame,
            text="CTkButton",
            compound="top",
        )
        self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.home_frame_button_4 = customtkinter.CTkButton(
            self.home_frame,
            text="CTkButton",
            compound="bottom",
            anchor="w",
        )
        self.home_frame_button_4.grid(row=2, column=2, padx=20, pady=10)

        self.select_frame_by_name("home")

    def button_callback(self):
        print("button pressed")

    def select_frame_by_name(self, name):
        self.home_button.configure(
            fg_color=("gray75", "gray25") if name == "home" else "transparent"
        )
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")