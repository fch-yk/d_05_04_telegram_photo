from random import randint
from datetime import datetime

import requests
from environs import Env

from images_files import download_image


def fetch_epic_pictures(nasa_api_key, folder_name):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {'api_key': nasa_api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    cards_number = randint(5, 10)
    media_cards = response.json()[:cards_number]

    for number, media_card in enumerate(media_cards):
        image_name = media_card['image']
        image_date = datetime.fromisoformat(media_card['date'])
        formatted_date = image_date.strftime('%Y/%m/%d')
        base_url = 'https://api.nasa.gov/EPIC/archive/natural'
        url = f'{base_url}/{formatted_date}/png/{image_name}.png'
        download_image(url, folder_name, f'nasa_epic_{number}.png', payload)


def main():
    env = Env()
    env.read_env()
    nasa_api_key = env('NASA_API_KEY', 'DEMO_KEY')
    folder_name = env('IMAGES_FOLDER', 'images')
    fetch_epic_pictures(nasa_api_key, folder_name)


if __name__ == '__main__':
    main()
