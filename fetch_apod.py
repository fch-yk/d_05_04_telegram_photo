from random import randint

import requests
from environs import Env

from images_files import download_image, get_link_extension


def fetch_astronomy_pictures(nasa_api_key, folder_name):
    url = 'https://api.nasa.gov/planetary/apod'
    images_count = randint(30, 50)
    payload = {'api_key': nasa_api_key, 'count': images_count}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    media_cards = response.json()
    for number, media_card in enumerate(media_cards):
        if media_card['media_type'] != 'image':
            continue

        link = media_card['url']
        extension = get_link_extension(link)
        download_image(link, folder_name, f'nasa_apod_{number}{extension}')


def main():
    env = Env()
    env.read_env()
    nasa_api_key = env('NASA_API_KEY', 'DEMO_KEY')
    folder_name = env('IMAGES_FOLDER', 'images')
    fetch_astronomy_pictures(nasa_api_key, folder_name)


if __name__ == '__main__':
    main()
