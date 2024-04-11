import os
from typing import List
from typing import Dict

def add_game(game_id: str) -> None:
    #Given a game, add the game_id to a folder of the involved teams and the map played.
    game_csv_path = f'games/{game_id}.csv'

    date, teams, map = game_id.split(";")
    team_a, team_b = teams.split("-")
    dir_path_team_a = f'teams/{team_a}'
    dir_path_team_b = f'teams/{team_b}'
    dir_path_map = f'maps/{map}'

    for dir in [dir_path_team_a, dir_path_team_b, dir_path_map]:
        file_path = dir + f'/{game_id}.csv'
        with open(file_path, 'w') as file:
            file.write(game_id)
        os.symlink(game_csv_path, file_path)


def add_games(game_ids: List[str]) -> None:
    for game in game_ids:
        add_game(game)