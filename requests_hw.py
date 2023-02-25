import requests
import json
from deco import logger

@logger
def hero_info():
    heroes_list_id = [332, 655, 149]
    intelligence_dict = {}

    for hero in heroes_list_id:
        hero_dict = json.loads(requests.get(f'https://akabab.github.io/superhero-api/api/id/{hero}.json').content)
        intelligence_dict[hero_dict['name']] = int(hero_dict['powerstats']['intelligence'])

    return(
        f' Самый умный супергерой {max(intelligence_dict, key=intelligence_dict.get)} его интеллект: {max(intelligence_dict.values())}')


hero_info()

