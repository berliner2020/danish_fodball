import requests
from requests.exceptions import Timeout, ConnectionError
from . import config


def start_session() -> requests.Session:
    """Start a new SportsMonk API session."""
    # fields
    headers = {"Authorization": config.sportmonks_api_token}

    # http session request
    try:
        sportmonks_session = requests.Session()
        sportmonks_session.headers = headers

        return sportmonks_session

    except Timeout as timeout_exc:
        raise TimeoutError(
            f"The SportMonks session request has timed out."
        ) from timeout_exc

    except ConnectionError as connection_exc:
        raise ConnectionError(
            f"The SportMonks session request has experienced an error."
        ) from connection_exc
