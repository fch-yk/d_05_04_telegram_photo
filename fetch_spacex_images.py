import argparse

import requests
from environs import Env

from images_files import download_image


def create_input_args_parser():
    description = 'The script downloads photoes from  SpaceX'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument(
        '--launch_id',
        metavar='{launch id}',
        help='launch id (e.g.: 5eb87d47ffd86e000604b38a), latest by default',
        default='latest'
    )

    return parser


def fetch_spacex_last_launch(launch_id, folder_name):
    base_url = 'https://api.spacexdata.com/v5/launches/'
    url = f'{base_url}{launch_id}'
    response = requests.get(url)
    response.raise_for_status()
    img_links = response.json()['links']['flickr']['original']
    for number, link in enumerate(img_links):
        download_image(link, folder_name, f'spacex_{number}.jpg')


def main():
    input_args_parser = create_input_args_parser()
    launch_id = input_args_parser.parse_args().launch_id
    env = Env()
    env.read_env()
    folder_name = env('IMAGES_FOLDER', 'images')
    fetch_spacex_last_launch(launch_id, folder_name)


if __name__ == '__main__':
    main()
