"""
Parse data from SierraLauncher.ini files.
"""
import re


class GameList:
    "Convert SierraLauncher.ini files to list of dicts."
    def __init__(self, ini_path: str) -> None:
        self.games_list = []
        self.ini_data = self.get_ini_data(ini_path)
        self.games_list = self.create_game_list()

    def get_ini_data(self, path):
        "Read data from Sierra INI file"
        with open(path, 'r', encoding='utf-8') as f:
            data = f.read()
        return data

    def create_game_list(self):
        "Creates list from Sierra INI file"
        _game_list = []
        sections = self.ini_data.split('\n\n')
        for section in sections:
            section_dict = self.parse_ini_data(section)
            if section_dict:
                _game_list.append(section_dict)
        return _game_list

    def parse_ini_data(self, sec):
        "Convert game INI section to dict"
        game = {}
        for line in sec.splitlines():
            if '=' in line:
                key, value = line.split('=')
                if re.match(r'^Game[0-9]', key):
                    key = re.sub('^Game[0-9]', '', key).lower()
                    value = value.replace('"', '')
                    game[key] = value
        return game

    def len(self) -> int:
        "Returns length of list"
        return self.games_list.__len__

    def print_games_list(self):
        "Output game list to console"
        for game in self.games_list:
            print(game.get('name'))
            for key in game:
                print(f"{key} - {game[key]}")
