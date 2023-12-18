import pandas as pd

from scraper.table_scraper.table_text_formatter import format_cell_text


def tables_soup_to_dataframes(tables_soup):
    dataframes = []
    for table in tables_soup:
        dataframe = table_soup_to_dataframe(table)
        if dataframe is not None:
            dataframes.append(dataframe)
    return dataframes


def table_soup_to_dataframe(table_soup):
    table_rows = table_soup.find_all("tr")

    table_headers = table_rows[0].find_all("th")
    table_cells = extract_table_cells(table_rows)

    table_headers = extract_text_table_headers(table_headers)
    table_cells = extract_text_table_cells(table_cells)

    try:
        dataframe = pd.DataFrame(table_cells, columns=table_headers)
    except ValueError as e:
        return None

    return dataframe


def extract_table_cells(table_rows):
    return [table_row.find_all("td") for table_row in table_rows]


def extract_text_table_headers(table_headers):
    headers = [header.text.strip() for header in table_headers]
    return headers


def extract_text_table_cells(table_cells):
    table_cells_text = []

    for row in table_cells:
        row_cells_text = [format_cell_text(cell.text) for cell in row if cell]

        if row_cells_text:
            table_cells_text.append(row_cells_text)

    return table_cells_text
