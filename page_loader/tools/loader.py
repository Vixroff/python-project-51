import os
from urllib.parse import urlparse, urljoin


from progress.bar import IncrementalBar


from page_loader.log import logger


from page_loader.tools.parser import parse
from page_loader.tools.names import get_folder_name, get_source_filename


SOURCES_ATR = {
    'img': 'src',
    'link': 'href',
    'script': 'src'
}


def create_source_folder(directory, url):
    folder_name = get_folder_name(url)
    path_to_folder = os.path.join(directory, folder_name)
    if not os.path.exists(path_to_folder):
        os.mkdir(path_to_folder)
    return path_to_folder


def check_link(link, url):
    if not link:
        return False
    link_netloc = urlparse(link).netloc
    url_netloc = urlparse(url).netloc
    return not link_netloc or link_netloc == url_netloc


def get_full_link(link, url):
    scheme = urlparse(url).scheme
    netloc = urlparse(url).netloc
    path = urlparse(link).path
    link = urljoin(f"{scheme}://{netloc}", path)
    return link


def save_source(source, link, folder_path):
    source_filename = get_source_filename(link)
    path_to_source_file = os.path.join(folder_path, source_filename)
    with open(path_to_source_file, 'wb') as w:
        w.write(source)
    return path_to_source_file


def download_sources(soup, url, directory):
    sources = soup.find_all(SOURCES_ATR.keys())
    bar = IncrementalBar('Loading sources', max=len(sources), suffix='%(percent).1f%% - %(max)d sources')
    folder_path = create_source_folder(directory, url)
    for source in sources:
        bar.next()
        atr = SOURCES_ATR.get(source.name)
        link = source.get(atr)
        if not link:
            logger.warning(f"No link here {link}")
            continue
        elif not check_link(link, url) is True:
            logger.warning(f"Link out of domain {link}")
            continue
        else:
            full_link = get_full_link(link, url)
            content = parse(full_link)
            path_to_source = save_source(content, full_link, folder_path)
            source[atr] = os.path.relpath(path_to_source, directory)
    bar.finish()
    return soup
