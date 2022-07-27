import os
from pathlib import Path
from random import shuffle
from time import sleep

import telegram
from environs import Env


def main():
    env = Env()
    env.read_env()
    with env.prefixed("TELEGRAM_"):
        bot_token = env('TOKEN')
        channel_id = env('CHANNEL_ID')
        upload_delay = env.int('UPLOAD_DELAY', 14400)
    bot = telegram.Bot(token=bot_token)
    max_file_size = 20971520
    while True:
        directories_content = os.walk('images')
        for folder_path, __, files_names in directories_content:
            shuffle(files_names)
            for file_name in files_names:
                file_path = os.path.join(folder_path, file_name)
                file_size = Path(file_path).stat().st_size
                if file_size > max_file_size:
                    continue
                with open(file_path, 'rb') as image:
                    bot.send_document(chat_id=channel_id, document=image)
                sleep(upload_delay)


if __name__ == '__main__':
    main()
