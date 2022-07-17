from random import randint

import requests
from environs import Env

from save_images import download_image


def fetch_epic_pictures(nasa_api_key):
    folder_name = 'images'
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {'api_key': nasa_api_key}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    cards_number = randint(5, 10)
    media_cards = response.json()[:cards_number]

    for number, media_card in enumerate(media_cards):
        image_name = media_card['image']
        image_date = media_card['date']
        year, month, day = image_date.split()[0].split(sep='-')
        base_url = 'https://api.nasa.gov/EPIC/archive/natural'
        url = f'{base_url}/{year}/{month}/{day}/png/{image_name}.png'
        download_image(url, folder_name, f'nasa_epic_{number}.png', payload)


def main():
    env = Env()
    env.read_env()
    nasa_api_key = env('NASA_API_KEY', 'DEMO_KEY')
    fetch_epic_pictures(nasa_api_key)


if __name__ == '__main__':
    main()
