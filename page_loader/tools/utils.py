import os
import re
from urllib.parse import urlparse


def modify_str(stroke):
    """
    Function modifies string object. Changes "\W" symbols to '-'
    """
    result = re.sub(r"[\W]", '-', stroke)
    return result


def split_url(url):
    """
    Function parses url and split it to meaning parts
    Returns tuple object where:
    tuple[0] == scheme;
    tuple[1] == netlock;
    tuple[2] == path;
    tuple[3] == extension
    """
    components = urlparse(url)
    scheme = components.scheme
    netloc = components.netloc
    path, extension = os.path.splitext(components.path)
    return scheme, netloc, path, extension


def create_source_link(tag_value, url):
    src_comps = split_url(tag_value)
    url_comps = split_url(url)
    if not src_comps[1]:
        link = f"{url_comps[0]}://{url_comps[1]}{src_comps[2]}{src_comps[3]}"
    else:
        link = f"{src_comps[0]}://{src_comps[1]}{src_comps[2]}{src_comps[3]}"
    return link


def get_html_filename(url):
    components = split_url(url)
    filename = modify_str(components[1]) + modify_str(components[2]) + '.html'
    return filename


def get_folder_name(url):
    components = split_url(url)
    folder_name = modify_str(components[1]) + modify_str(components[2]) + '_files'
    return folder_name


def get_source_filename(link):
    link_comp = split_url(link)
    source_filename = modify_str(link_comp[1]) + modify_str(link_comp[2]) + link_comp[3]
    return source_filename