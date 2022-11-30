import os
from bs4 import BeautifulSoup


from page_loader.tools.parser import parse_html, parse_source
from page_loader.tools.utils import get_html_filename, get_folder_name, get_source_filename, create_source_link


def download_sources(soup, url, directory):
    sources_folder_name = get_folder_name(url)
    path_to_folder = os.path.join(directory, sources_folder_name)
    if not os.path.exists(path_to_folder):
        os.mkdir(path_to_folder)
    sources = soup.find_all('img')
    for source in sources:
        tag_value = source.get('src')
        link = create_source_link(tag_value, url)
        source_binary = parse_source(link)
        if source_binary:
            source_filename = get_source_filename(link)
            path_to_source = os.path.join(path_to_folder, source_filename)
            source['src'] = os.path.join(sources_folder_name, source_filename)
            with open(path_to_source, 'wb') as e:
                e.write(source_binary)
    return soup


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
    html = parse_html(url)
    if html:
        path_to_output = get_path_to_output(output)
        html_soup = BeautifulSoup(html, 'html.parser')
        new_soup = download_sources(html_soup, url, path_to_output)
        path_to_html = save_html(new_soup, url, path_to_output)
        return path_to_html
