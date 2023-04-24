from decouple import config


def main():
    print(config('BOT_TOKEN'))


if __name__ == '__main__':
    main()
