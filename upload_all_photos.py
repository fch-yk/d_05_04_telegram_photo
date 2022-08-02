import sys
from random import shuffle
from time import sleep

import telegram
from environs import Env

from images_files import get_files_paths, filter_files_for_telegram


def main():
    env = Env()
    env.read_env()
    folder_name = env('IMAGES_FOLDER', 'images')
    with env.prefixed("TELEGRAM_"):
        bot_token = env('TOKEN')
        channel_id = env('CHANNEL_ID')
        upload_delay = env.int('UPLOAD_DELAY', 14400)
    bot = telegram.Bot(token=bot_token)
    error_delay = 1
    while True:
        files_paths = get_files_paths(folder_name)
        suitable_files_paths = filter_files_for_telegram(files_paths)
        shuffle(suitable_files_paths)
        for file_path in suitable_files_paths:
            try:
                with open(file_path, 'rb') as image:
                    bot.send_document(chat_id=channel_id, document=image)
                sleep(upload_delay)
                error_delay = 1
            except telegram.error.NetworkError as fail:
                print(f'Unable to send a message: {fail}', file=sys.stderr)
                sleep(error_delay)
                error_delay = 15


if __name__ == '__main__':
    main()
