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
    directories_content = os.walk(folder_name)
    for folder_path, __, files_names in directories_content:
        for file_name in files_names:
            file_path = os.path.join(folder_path, file_name)
            files_paths.append(file_path)
    return files_paths


def filter_files_for_telegram(files_paths):
    max_size = 20971520
    return [
        file_path for file_path in files_paths
        if Path(file_path).stat().st_size <= max_size
    ]
