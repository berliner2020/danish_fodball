import django
import sportsmonk_session


def execute():
    sportsmonk_session.start_session()

    # http request
    sportmonk_session = s.get(url=base_url)
    print(sportmonk_session.status_code)

if __name__ == '__main__':
    execute()

