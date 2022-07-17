from environs import Env
import telegram


def main():
    env = Env()
    env.read_env()
    bot_token = env('TELEGRAM_TOKEN')
    bot = telegram.Bot(token=bot_token)
    print(bot.get_me())


if __name__ == '__main__':
    main()
