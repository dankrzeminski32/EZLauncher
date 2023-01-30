import os
# Use the command below to run a Steam game
# subprocess.call(r"C:\Program Files (x86)\Steam\Steam.exe -applaunch 578080")
# 578080 represents the steam ID
# C:\Program Files (x86)\Steam\steamapps\appmanifest_id -> is where you find the steam games and all their id's/information
# We'll need to parse those files for the ids and then use them in the subprocess command



class SteamGame:
    def __init__(self, id:str, game_title:str):
        self.id = id
        self.game_title = game_title
    
    def __repr__(self):
       return 'SteamGame(%s, %s)' % (self.id, self.game_title)    
  
    def __str__(self):
       return 'id: %s game_title: %s' % (self.id, self.game_title)    
        
class SteamGameFinder:
    def __init__(self, steam_app_folder:str="C:\Program Files (x86)\Steam\steamapps"):
        self.steam_app_folder = steam_app_folder
        
    def _get_all_manifest_files(self) -> list[str]:
        manifest_file_locations: list[str] = []
        for filename in os.listdir(self.steam_app_folder):
            file_path = os.path.join(self.steam_app_folder, filename)
            # checking if it is a file
            if os.path.isfile(file_path) and filename[-3:]=='acf':
                manifest_file_locations.append(file_path)
        return manifest_file_locations
    
    def _parse_game_id_line(self, line: str) -> str:
        return line.split('"')[3]
        
    def _parse_game_title_line(self, line:str) -> str:
        return line.split('"')[3]

    def get_installed_games_info(self) -> list[SteamGame]:
        manifest_file_paths: list[str] = self._get_all_manifest_files()
        all_games_info: list[SteamGame] = []
        for file in manifest_file_paths:
            f = open(file, "r")
            for idx, line in enumerate(f):
                if idx==2:
                    game_id = self._parse_game_id_line(line)
                if idx==5:
                    game_title = self._parse_game_title_line(line)
            steam_game = SteamGame(game_id, game_title)
            all_games_info.append(steam_game)
            
        return all_games_info
                
                    
                

#Uncomment these lines for module example
#steam_app_folder = r"C:\Program Files (x86)\Steam\steamapps"
#steam_parser = SteamGameFinder(steam_app_folder=steam_app_folder)
#print(steam_parser.get_installed_games_info())
#import subprocess
#subprocess.call(r"C:\Program Files (x86)\Steam\Steam.exe -applaunch 228980")