import argparse
import os
from random import choice

import telegram
from environs import Env


def create_input_args_parser():
    description = (
        'Uploads a photo from "images" folder to your Telegram channel.'
    )
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument(
        '--file_name',
        metavar='{file name}',
        help='file name (e.g.: nasa_apod_0.jpg), a random file by default',
        default=choice(list(os.walk('images'))[0][-1])
    )

    return parser


def main():
    env = Env()
    env.read_env()
    with env.prefixed("TELEGRAM_"):
        bot_token = env('TOKEN')
        channel_id = env('CHANNEL_ID')

    bot = telegram.Bot(token=bot_token)
    input_args_parser = create_input_args_parser()
    file_name = input_args_parser.parse_args().file_name

    file_path = os.path.join('images', file_name)
    with open(file_path, 'rb') as image:
        bot.send_document(chat_id=channel_id, document=image)


if __name__ == '__main__':
    main()
