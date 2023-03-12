import requests
import config


def start_session():
    # fields
    base_url = "https://api.sportmonks.com/v3/football/fixtures"
    headers = {"Authorization": config.sportsmonk_api_token}
    # query_str_parameters = {"include": "statistics"}

    # http session
    try:
        s = requests.Session()
        s.headers = headers

        # http request
        r = s.get(url=base_url)
        print(r.status_code)

    except requests.exceptions.Timeout as timeout_error:
        print(f"portsMonk session timed out: {timeout_error}")
        raise timeout_error
    except requests.exceptions.TooManyRedirects as redirects_error:
        print(f"portsMonk session timed out: {redirects_error}")
        raise redirects_error
    except ConnectionError as connection_error:
        print(f"Unable to start SportsMonk session: {connection_error}")
        raise connection_error
