import requests
from config.settings import API_KEY, BASE_URL


def get_news(country, category, keyword, page_size):

    params = {
        "apiKey": API_KEY,
        "country": country,
        "category": category,
        "pageSize": page_size
    }

    if keyword:
        params["q"] = keyword

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        return response.json()

    return None