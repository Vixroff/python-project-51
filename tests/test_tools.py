from page_loader.tools.formatter import create_filename


def test_create_filename():
    assert create_filename('https://ru.hexlet.io/courses') == 'ru-hexlet-io-courses.html'