import json

from crawl_websummit_startups import output_filename


def analyze():
    with open(output_filename, 'r') as file:
        companies = json.loads(file.read())

    companies_with_facebook = [company for company in companies if "facebook" in company]
    print("With facebook:", len(companies_with_facebook))

    companies_with_instagram = [company for company in companies if "instagram" in company]
    print("With instragram:", len(companies_with_instagram))

    companies_with_twitter = [company for company in companies if "twitter" in company]
    print("With twitter:", len(companies_with_twitter))

    companies_with_website = [company for company in companies if "website" in company]
    print("With website:", len(companies_with_website))


if __name__ == '__main__':
    analyze()
