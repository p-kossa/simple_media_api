from config import Config
import requests
import json


moviedb_api_key = Config.MOVIEDB_API_KEY
moviedb_base_url = Config.MOVIEDB_BASE_URL


def get_index_movies() -> None:
    r = requests.get(
        '{}discover/movie?api_key={}&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1'
        .format(moviedb_base_url, moviedb_api_key))

    with open('data.json', 'w') as f:
        json.dump(r.text, f, sort_keys=True, indent=4)
