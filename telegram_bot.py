from environs import Env
import telegram


def main():
    env = Env()
    env.read_env()
    with env.prefixed("TELEGRAM_"):
        bot_token = env('TOKEN')
        channel_id = env('CHANNEL_ID')
    bot = telegram.Bot(token=bot_token)
    with open('images/nasa_epic_2.png', 'rb') as image:
        bot.send_document(chat_id=channel_id, document=image)


if __name__ == '__main__':
    main()
