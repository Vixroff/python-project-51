import os
import re
from urllib.parse import urlparse


def modify_str(stroke):
    """
    Function modifies string object. Changes "\\W" symbols to '-'
    """
    result = re.sub(r'[\W]', '-', stroke)
    return result


def get_filename(url):
    netloc = urlparse(url).netloc
    path, extension = os.path.splitext(urlparse(url).path)
    if not extension:
        extension = '.html'
    filename = modify_str(netloc) + modify_str(path) + extension
    return filename


def get_folder_name(url):
    netloc = urlparse(url).netloc
    path = urlparse(url).path
    folder_name = modify_str(netloc) + modify_str(path) + '_files'
    return folder_name
