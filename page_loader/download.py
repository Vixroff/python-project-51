import os
import requests


from page_loader.tools.formatter import create_filename


def download(directory, url):
    response = requests.get(url)
    data = response.text
    filename = create_filename(url)
    if directory == 'current':
        directory = os.getcwd()
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as w:
        w.write(data)
    return filepath
