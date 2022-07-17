import os
from pathlib import Path
from urllib.parse import unquote, urlsplit

import requests


def download_image(url, folder_name, file_name, payload=None):
    Path(folder_name).mkdir(exist_ok=True)
    file_path = os.path.join(folder_name, file_name)

    response = requests.get(url, params=payload)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        file.write(response.content)


def get_link_extension(link):
    path = urlsplit(link).path
    unquouted_path = unquote(path)
    return os.path.splitext(unquouted_path)[1]
