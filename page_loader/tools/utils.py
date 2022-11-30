import os
import re
from urllib.parse import urlparse


def modify_str(stroke):
    """
    Function modifies string object. Changes "\W" symbols to '-'
    """
    regex = r"[\W]"
    result = re.sub(regex, '-', stroke)
    return result


def get_html_filename(url):
    netloc = urlparse(url).netloc
    path = os.path.splitext(urlparse(url).path)
    filename = modify_str(netloc) + modify_str(path[0]) + '.html'
    return filename


def get_folder_name(url):
    netloc = urlparse(url).netloc
    path = urlparse(url).path
    folder_name = modify_str(netloc) + modify_str(path) + '_files'
    return folder_name


def get_source_filename(link):
    netloc = urlparse(link).netloc
    path, extension = os.path.splitext(urlparse(link).path)
    source_filename = modify_str(netloc) + modify_str(path) + extension
    return source_filename
