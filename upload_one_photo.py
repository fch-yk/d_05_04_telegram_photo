import argparse
from random import choice

import telegram
from environs import Env

from images_files import get_files_paths


def create_input_args_parser():
    description = (
        'Uploads a photo to your Telegram channel.'
    )
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument(
        '--file_path',
        metavar='{file path}',
        help=(
            'file path (e.g.: E:\tmp\nasa_apod_0.jpg), '
            'a random file from "Images" folder by default'
        ),
        default=choice(get_files_paths())
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
    file_path = input_args_parser.parse_args().file_path

    with open(file_path, 'rb') as image:
        bot.send_document(chat_id=channel_id, document=image)


if __name__ == '__main__':
    main()
