import os
from pathlib import Path
from urllib.parse import unquote, urlsplit

import requests


def download_image(url, folder_name, file_name, payload=None):
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    file_path = os.path.join(folder_name, file_name)

    response = requests.get(url, params=payload)
    response.raise_for_status()

    with open(file_path, 'wb') as file:
        file.write(response.content)


def get_link_extension(link):
    path = urlsplit(link).path
    unquoted_path = unquote(path)
    return os.path.splitext(unquoted_path)[1]


def get_files_paths(folder_name):
    files_paths = []
    max_file_size = 20971520
    directories_content = os.walk(folder_name)
    for folder_path, __, files_names in directories_content:
        for file_name in files_names:
            file_path = os.path.join(folder_path, file_name)
            file_size = Path(file_path).stat().st_size
            if file_size > max_file_size:
                continue
            files_paths.append(file_path)

    return files_paths
