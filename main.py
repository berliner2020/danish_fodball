import django
import sportsmonk_session


def execute():
    # start api session
    sportsmonk_session.start_session()

    # http request fields
    base_url = ""

    # http request
    r = sportsmonk_session.get(url=base_url)
    print(r.status_code)


if __name__ == '__main__':
    execute()

