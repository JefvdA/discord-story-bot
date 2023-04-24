from decouple import config
from story_bot import bot


def main():
    bot.run(config('BOT_TOKEN'))


if __name__ == '__main__':
    main()
