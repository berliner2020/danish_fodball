from football_app import sportmonks_session


def execute():
    # start api session
    sportmonks_session.start_session()
    # query_str_parameters = {"include": "statistics"}

    # http request fields
    base_url = "https://api.sportmonks.com/v3/football/fixtures"

    # http request
    r = sportmonks_session.get(url=base_url)
    print(r.status_code)


if __name__ == '__main__':
    execute()

