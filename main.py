import django
import sportsmonk_session


def execute():
    sportsmonk_session.start_session()


if __name__ == '__main__':
    execute()

