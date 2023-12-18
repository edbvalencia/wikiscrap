from bs4 import BeautifulSoup as bs

from scraper.requester import make_request
from scraper.table_scraper.table_formatter import tables_soup_to_dataframes


def get_dataframes_tables_from_url(url):
    response_data = make_request(url)

    if not response_data:
        return None

    tables_titles, tables_soup = extract_tables_soup_from_response(response_data)
    return tables_titles, tables_soup_to_dataframes(tables_soup)


def extract_tables_soup_from_response(response_data):
    tables_titles = []
    tables_soup = []

    for section in response_data.get("sections", []):
        section_text = section.get("text", "")  # puede o no tener una tabla
        title_table = section.get("line", "")
        soup = bs(section_text, "html.parser")
        table_soup = soup.find("table")

        if table_soup and is_valid_table(soup):
            tables_titles.append(title_table)
            tables_soup.append(table_soup)

    return tables_titles, tables_soup


def is_valid_table(soup):
    rows = soup.find_all("tr")

    if len(rows) < 2:
        return False

    number_headers_first_row = len(rows[0].find_all("th"))
    number_total_headers = len(soup.find_all("th"))

    if number_headers_first_row != number_total_headers:
        return False

    number_total_data = len(soup.find_all("td"))

    if number_total_data % number_headers_first_row != 0:
        return False

    return True
