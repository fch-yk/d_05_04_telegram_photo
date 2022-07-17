from random import randint

import requests
from environs import Env

from save_images import download_image, get_link_extension


def fetch_astronomy_pictures(nasa_api_key):
    folder_name = 'images'
    url = 'https://api.nasa.gov/planetary/apod'
    images_count = randint(30, 50)
    payload = {'api_key': nasa_api_key, 'count': images_count}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    media_cards = response.json()
    for number, media_card in enumerate(media_cards):
        link = media_card.get('url', None)
        if media_card['media_type'] != 'image' or link is None:
            continue

        extension = get_link_extension(link)
        download_image(link, folder_name, f'nasa_apod_{number}{extension}')


def main():
    env = Env()
    env.read_env()
    nasa_api_key = env('NASA_API_KEY', 'DEMO_KEY')
    fetch_astronomy_pictures(nasa_api_key)


if __name__ == '__main__':
    main()
