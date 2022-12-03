import os
import tempfile
import pytest


import requests


from page_loader.download import download


URL = 'https://ru.hexlet.io/courses'
SRC = 'https://ru.hexlet.io/assets/professions/nodejs.png'


def read(path, mode='r'):
    with open(path, mode) as f:
        result = f.read()
    return result


def test_download(requests_mock):
    """
    Test the main function 'download' of 'page-loader' library.
    It checks content and file's existing at specified directory 

    """
    requests_mock.get(URL, text=read('tests/fixtures/original.html'))
    requests_mock.get(SRC, content=read('tests/fixtures/files/image.png', 'rb'))
    with tempfile.TemporaryDirectory() as tmpdir:
        actual_output = download(tmpdir, URL)
        expected_output_data = read('tests/fixtures/expected.html')
        source_path = os.path.join(tmpdir, 'ru-hexlet-io-courses_files/ru-hexlet-io-assets-professions-nodejs.png')
        assert os.path.exists(actual_output)
        assert os.path.exists(source_path)
        assert read(source_path, 'rb') == read('tests/fixtures/files/image.png', 'rb')
        assert read(actual_output) == expected_output_data


@pytest.mark.parametrize('exception', [
    requests.HTTPError, requests.ConnectionError,
    requests.URLRequired, requests.TooManyRedirects, requests.Timeout,
    PermissionError, FileNotFoundError])
def test_download_exceptions(exception, tmpdir, requests_mock):
    with pytest.raises(exception):
        requests_mock.get(URL, exc=exception)
        download(tmpdir, URL)