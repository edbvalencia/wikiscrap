import requests

from scraper.constans import COOKIES, HEADERS

TIMEOUT = 3


def make_request(url: str):
    try:
        response = requests.get(url, cookies=COOKIES, headers=HEADERS, timeout=TIMEOUT)
        response.raise_for_status()
        response_data = response.json()
        return response_data
    except requests.exceptions.RequestException as e:
        print(f"Error making request to {url}: {e}")
        return None
