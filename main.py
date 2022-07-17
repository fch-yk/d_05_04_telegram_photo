import os
from pathlib import Path
from pprint import pprint
from random import randint
from urllib.parse import urlsplit, unquote


from environs import Env
import requests


def download_image(url, folder_name, file_name, payload=None):
    Path(folder_name).mkdir(exist_ok=True)
    file_path = os.path.join(folder_name, file_name)

    response = requests.get(url, params=payload)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(folder_name):
    url = 'https://api.spacexdata.com/v5/launches/5eb87d47ffd86e000604b38a'
    response = requests.get(url)
    response.raise_for_status()
    img_links = response.json()['links']['flickr']['original']
    for number, link in enumerate(img_links):
        download_image(link, folder_name, f'spacex_{number}.jpg')


def get_link_extension(link):
    path = urlsplit(link).path
    unquouted_path = unquote(path)
    return os.path.splitext(unquouted_path)[1]


def fetch_astronomy_pictures(nasa_api_key, folder_name):
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


def fetch_epic_pictures(nasa_api_key, folder_name):
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
    folder_name = 'images'
    fetch_epic_pictures(nasa_api_key, folder_name)

    # fetch_astronomy_pictures(nasa_api_key, folder_name)


if __name__ == '__main__':
    main()
