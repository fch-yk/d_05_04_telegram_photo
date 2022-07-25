from environs import Env
import telegram


def main():
    env = Env()
    env.read_env()
    with env.prefixed("TELEGRAM_"):
        bot_token = env('TOKEN')
        channel_id = env('CHANNEL_ID')
    bot = telegram.Bot(token=bot_token)
    bot.send_message(chat_id=channel_id, text="Hello, space channel!")


if __name__ == '__main__':
    main()
