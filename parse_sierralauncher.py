import re


class GameList:
    def __init__(self, ini_path: str) -> None:
        self.ini_data = self.get_ini_data(ini_path)
        self.games_list = self.create_game_list()

    def get_ini_data(self, path):
        with open(path, 'r', encoding='utf-8') as f:
            data = f.read()
        return data

    def create_game_list(self):
        _game_list = []
        sections = self.ini_data.split('\n\n')
        for section in sections:
            section_dict = self.parse_ini_data(section)
            if section_dict:
                _game_list.append(section_dict)
        return _game_list

    def parse_ini_data(self, sec):
        g = {}
        for line in sec.splitlines():
            if '=' in line:
                key, value = line.split('=')
                if re.match(r'^Game[0-9]', key):
                    key = re.sub('^Game[0-9]', '', key).lower()
                    value = value.replace('"', '')
                    g[key] = value
        return g

    def get_games_list(self):
        return self.games_list

    def print_games_list(self):
        for game in self.games_list:
            print(game.get('name'))
            for k in game:
                print(f"{k} - {game[k]}")
