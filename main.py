from decouple import config
from story_bot import client


def main():
    client.run(config('BOT_TOKEN'))


if __name__ == '__main__':
    main()
