from random import shuffle
from time import sleep

import telegram
from environs import Env

from images_files import get_files_paths


def main():
    env = Env()
    env.read_env()
    folder_name = env('IMAGES_FOLDER', 'images')
    with env.prefixed("TELEGRAM_"):
        bot_token = env('TOKEN')
        channel_id = env('CHANNEL_ID')
        upload_delay = env.int('UPLOAD_DELAY', 14400)
    bot = telegram.Bot(token=bot_token)
    while True:
        files_paths = get_files_paths(folder_name)
        shuffle(files_paths)
        for file_path in files_paths:
            with open(file_path, 'rb') as image:
                bot.send_document(chat_id=channel_id, document=image)
            sleep(upload_delay)


if __name__ == '__main__':
    main()
