import customtkinter
from src.games.steam import SteamGameFinder

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("EZLauncher")
        self.minsize(1200, 750)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0,weight=1)
        self.grid_columnconfigure(1, weight=8)
        

        ####### CENTER GAME LIBRARY #######
        self.game_library_frame = customtkinter.CTkFrame(self, width=700, height=600)
        self.game_library_frame.grid(row=0,column=1)
        self.game_library_frame.grid_columnconfigure(0,weight=1)
        self.game_library_frame.grid_rowconfigure(0,weight=1)
        
        
        self.game_library_title_label = customtkinter.CTkLabel(self.game_library_frame, text="Steam Games - Subject to Change", font=customtkinter.CTkFont(size=25, weight="bold"))
        self.game_library_title_label.grid(row=0,column=0,padx=20, pady=20)
        
        self.game_library_game_list_frame = customtkinter.CTkFrame(self.game_library_frame, width=700, height=550)
        self.game_library_game_list_frame.grid(row=1,column=0,padx=20, pady=20)
        self.display_steam_games(self.game_library_game_list_frame)

        ####### NAVIGATION SIDE PANEL #######
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")

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
            text="Home",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
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
        
    def display_steam_games(self, frame: customtkinter.CTkFrame):
        game_finder = SteamGameFinder()
        steam_games = game_finder.get_installed_games_info()
        for idx,game in enumerate(steam_games,start=2):
            setattr(self, game.id, customtkinter.CTkLabel(frame, text=game.game_title, font=customtkinter.CTkFont(size=13, weight="bold")))
            getattr(self, game.id).grid(row=idx,column=0,padx=30, pady=30)