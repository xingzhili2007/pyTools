import os
import requests


def download_file(url, store_path):
    filename = url.split("/")[-1]
    filepath = os.path.join(store_path, filename)

    file_data = requests.get(url, allow_redirects=True).content
    with open(filepath, 'wb') as handler:
        handler.write(file_data)
