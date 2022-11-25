import os
import tempfile

from page_loader import download
from page_loader.tools.reader import read


URL = 'https://ru.hexlet.io/courses'


def test_download(requests_mock):
    """Test download function - the main function of page-loader library"""
    expected_file = read('tests/fixtures/expected.html')
    requests_mock.get(URL, text=expected_file)
    with tempfile.TemporaryDirectory() as tmpdir:
        actual_path = download(tmpdir, URL)
        assert os.path.exists(actual_path)
        assert read(actual_path) == expected_file
