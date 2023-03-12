import requests
import config


def start_session():
    # fields
    base_url = "https://api.sportmonks.com/v3/football/fixtures"
    headers = {"Authorization": config.sportsmonk_api_token}
    # query_str_parameters = {"include": "statistics"}

    # http session
    s = requests.Session()
    s.headers = headers

    # http request
    r = s.get(url=base_url)
    print(r.status_code)
