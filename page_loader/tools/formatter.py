import re


def create_filename(url):
    url = re.sub(r"https?:\/\/", "", url)
    url = re.sub(r"[\W](?!html)", '-', url)
    if not url.endswith('html'):
        url = url + '.html'
    return url
