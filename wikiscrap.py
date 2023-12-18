from scraper.table_scraper.table_scraper import get_dataframes_tables_from_url
from scraper.table_scraper.table_utils import browser_url_to_api_endpoint


def get_dataframes_tables_from_browser_url(browser_url):
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
