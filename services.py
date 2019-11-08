import csv
import json

from crawl_websummit_startups import output_filename


def get_companies_from_json():
    """
    Returns a list of companies dicts that is stored in the local json.
    :return:
    """
    with open(output_filename, "r") as file:
        companies = json.loads(file.read())
    return companies


def get_columns():
    """
    Returns a superset of all keys that can contain in a company dict.
    :return:
    """
    columns = []
    companies = get_companies_from_json()
    for company in companies:
        for key in company.keys():
            if key not in columns:
                columns.append(key)
    return columns


def to_csv():
    csv_filename = 'websummit2019startups.csv'
    companies = get_companies_from_json()

    csv_columns = get_columns()
    try:
        with open(csv_filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in companies:
                writer.writerow(data)
    except IOError:
        print("I/O error")
