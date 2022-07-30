# Space photos for Telegram

The project scripts can be used for downloading space photos and uploading them to your Telegram channel.

## Prerequisites

Python 3.10 or higher required.

## Installing

- Download the project files
- Set up packages:

```bash
pip install -r requirements.txt
```

- Set up environmental variables in your operating system or in .env file. The variables are:
  - `NASA_API_KEY` is used for authorization at [NASA APIs](https://api.nasa.gov/)
  - `TELEGRAM_TOKEN` is used to manage your telegram bot
  - `TELEGRAM_CHANNEL_ID` is the ID of your telegram channel
  - `TELEGRAM_UPLOAD_DELAY` is a pause between photo uploads (sec); default value: 14400 sec (4 hours)
  - `IMAGES_FOLDER` is a path to a folder containing images; default value: images.
      1. You can specify a relative path, e.g.: my_images. In this case, the folder is in the root folder of the project.
      2. You can specify an absolute path, e.g.: E:\tmp\images.

To set up variables in .env file, create it in the root directory of the project and fill it up like this:

```bash
NASA_API_KEY=yournasaaipkey
TELEGRAM_TOKEN=yourbottoken
TELEGRAM_CHANNEL_ID=@example_channel
TELEGRAM_UPLOAD_DELAY=15000
IMAGES_FOLDER=my_images
```

## Scripts that download pictures

These scripts download pictures to the folder (see `IMAGES_FOLDER` in the section [Installing](#installing))

### Script "fetch_apod"

- Can download 30-50 pictures from [Astronomy Picture of the Day](https://apod.nasa.gov/apod/astropix.html)

- Run:

```bash
python fetch_apod.py
```

### Script "fetch_epic_images"

- Can download 5-10 pictures from [EPIC](https://epic.gsfc.nasa.gov/)

- Run:

```bash
python fetch_epic_images.py
```

### Script "fetch_spacex_images"

- Can download pictures using [SpaceX-API](https://github.com/r-spacex/SpaceX-API)

- To download pictures of the latest launch, run:

```bash
python fetch_spacex_images.py
```

- To download pictures by the launch ID, run:

```bash
python fetch_spacex_images.py --launch_id 5eb87d47ffd86e000604b38a
```

where `5eb87d47ffd86e000604b38a` is a launch ID

## Scripts that upload pictures to your telegram channel

These scripts use your Telegram bot to upload pictures from the "images folder" (and all its subfolders) to your Telegram channel. Environment variables `TELEGRAM_TOKEN`, `TELEGRAM_CHANNEL_ID` and `IMAGES_FOLDER` should be set, see the section [Installing](#installing)

### Script "upload_all_photos"

- Uploads pictures with a pause, see `TELEGRAM_UPLOAD_DELAY` in the section [Installing](#installing)

- Run:

```bash
python upload_all_photos.py
```

### Script "upload_one_photo"

- To upload a random photo, run:

```bash
python upload_one_photo.py
```

- To upload a specified image file, run:

```bash
python upload_one_photo.py --file_path E:\tmp\nasa_apod_0.jpg
```

where `E:\tmp\nasa_apod_0.jpg` is an absolute file path

## Project goals

The project was created for educational purposes.
It's a lesson for python and web developers at [Devman](https://dvmn.org)
