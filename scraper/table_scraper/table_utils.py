from scraper.constans import API_URL


def rename_empty_headers(dataframe):
    renamed_columns = []
    i = 0
    for column in dataframe.columns:
        if column == "":
            i += 1
            renamed_columns.append(f"Unnamed_{i}")
        else:
            renamed_columns.append(column)

    dataframe.columns = renamed_columns
    return dataframe


def browser_url_to_api_endpoint(browser_url):
    url_parts = browser_url.split("/")
    last_path_segment = url_parts[-1]
    api_endpoint_url = f"{API_URL}{last_path_segment}"
    return api_endpoint_url


def export_dataframe_json(dataframe):
    json_filename = "table.json"
    rename_empty_headers(dataframe)
    dataframe.to_json(
        json_filename, orient="records", lines=False, indent=2, force_ascii=False
    )
    print(f"Saved {json_filename}")


def export_dataframe_csv(dataframe):
    csv_filename = "table.csv"
    dataframe.to_csv(csv_filename, index=False, encoding="utf-8")
    print(f"Saved {csv_filename}")
