import os
from bs4 import BeautifulSoup


from page_loader.tools.parser import parse
from page_loader.tools.loader import download_sources
from page_loader.tools.utils import get_html_filename


def save_html(soup, url, directory):
    html_filename = get_html_filename(url)
    path_to_html = os.path.join(directory, html_filename)
    soup = soup.prettify()
    with open(path_to_html, 'w') as f:
        f.write(soup)
    return path_to_html


def get_path_to_output(output):
    if output == "current":
        path = os.getcwd()
    elif os.path.exists(output):
        path = output
    else:
        raise NotADirectoryError("Directory not found")
    return path


def download(output, url):
    html = parse(url)
    if html:
        path_to_output = get_path_to_output(output)
        html_soup = BeautifulSoup(html, 'html.parser')
        new_soup = download_sources(html_soup, url, path_to_output)
        path_to_html = save_html(new_soup, url, path_to_output)
        return path_to_html
