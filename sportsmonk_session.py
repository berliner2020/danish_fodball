import requests
import config


def start_session() -> requests.Session:
    # fields
    base_url = "https://api.sportmonks.com/v3/football/fixtures"
    headers = {"Authorization": config.sportsmonk_api_token}
    # query_str_parameters = {"include": "statistics"}

    # http session
    try:
        sportmonk_session = requests.Session()
        sportmonk_session.headers = headers

        # http request
        r = sportmonk_session.get(url=base_url)
        print(r.status_code)

        return sportmonk_session

    except requests.exceptions.Timeout as timeout_error:
        print(f"portsMonk session timed out: {timeout_error}")
        raise timeout_error
    except requests.exceptions.TooManyRedirects as redirects_error:
        print(f"portsMonk session timed out: {redirects_error}")
        raise redirects_error
    except ConnectionError as connection_error:
        print(f"Unable to start SportsMonk session: {connection_error}")
        raise connection_error
