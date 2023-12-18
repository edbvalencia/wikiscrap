from scraper.table_scraper.table_scraper import get_dataframes_tables_from_url
from scraper.table_scraper.table_utils import (
    browser_url_to_api_endpoint,
    export_dataframe_csv,
    export_dataframe_json,
)


def extract_tables_by_browser_url(browser_url):
    url_api_endpoint = browser_url_to_api_endpoint(browser_url)
    tables_titles, dataframes = get_dataframes_tables_from_url(url_api_endpoint)
    print_titles(tables_titles)
    return tables_titles, dataframes


def print_titles(tables_titles):
    for i, title in enumerate(tables_titles):
        print(f"{i} | {title}")


def get_dataframe_by_index(dataframes, index):
    for i, dataframe in enumerate(dataframes):
        if i == index:
            return dataframe
    return None


def save_to_json(dataframe):
    export_dataframe_json(dataframe)


def save_to_csv(dataframe):
    export_dataframe_csv(dataframe)


titles, dataframes = extract_tables_by_browser_url(
    "https://www.wikiwand.com/es/Anexo%3AEstad%C3%ADsticas_de_la_Copa_Libertadores"
)
