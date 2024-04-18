import jsonpickle
from jsonpickle import handlers


file_path = '/Users/leonma/Downloads/projections.json'
with open(file_path, 'r') as file:
    json_data = file.read()

data = jsonpickle.decode(json_data)
projections = data['data']
players = data['included']

cs_projections = []
cs_players = {}

for item in projections:
    if item['relationships']['league']['data']['id'] == "265":
        simplified_item = {
            "stat_type": item["attributes"]["stat_type"],
            "line_score": item["attributes"]["line_score"],
            "player_id": item["relationships"]["new_player"]["data"]["id"]
        }

        cs_projections.append(simplified_item)
        cs_players[item['relationships']['new_player']['data']['id']] = None

for item in players:
    if item['id'] in cs_players:
        cs_players[item['id']] = item
      
print(cs_projections)

    
