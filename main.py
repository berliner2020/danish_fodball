import config
import django
import requests


def execute():
    # fields
    base_url = "https://api.sportmonks.com/v3/football/fixtures"
    headers = {"Authorization": config.sportsmonk_api_token}
    # query_str_parameters = {"include": "statistics"}

    # http request
    r = requests.get(url=base_url, headers=headers)
    print(r.status_code)


if __name__ == '__main__':
    execute()

