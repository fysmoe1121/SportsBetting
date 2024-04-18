import jsonpickle
from jsonpickle import handlers


file_path = '/Users/leonma/Downloads/projections.json'
with open(file_path, 'r') as file:
    json_data = file.read()

data = jsonpickle.decode(json_data)
all_projections = data['data']
all_players = data['included']

cs_projections = []
cs_players = {}
new_players = set()

for projection in all_projections:
    if projection['relationships']['league']['data']['id'] == "265":
        simplified_projection = {
            "stat_type": projection["attributes"]["stat_type"],
            "line_score": projection["attributes"]["line_score"],
            "opposing_team": projection["attributes"]["description"],
            "player_id": projection["relationships"]["new_player"]["data"]["id"]
        }

        if not simplified_projection["player_id"] in cs_players:
            new_players.add(simplified_projection["player_id"])

        cs_projections.append(simplified_projection)

if new_players:
    for player in all_players:
        if player['id'] in new_players:
            simplified_player = {
                'name': player["attributes"]['name'],
                'team': player["attributes"]['team']
            }

            cs_players[player['id']] = simplified_player
            new_players.discard(player['id'])

for projection in cs_projections:
    projection['player_name'] = cs_players[projection['player_id']]['name']
    projection['player_team'] = cs_players[projection['player_id']]['team']
    print(projection, "\n")



#print(cs_projections)
#print(cs_players)
#print(new_players)
    
