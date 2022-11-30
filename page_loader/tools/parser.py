import requests


def parse_html(url):
    """
    This function makes request to url and returns html code or False if error there
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except(requests.RequestException, ValueError) as e:
        print(f'Unable to access the network\n{e}')
        return False


def parse_source(link):
    try:
        response = requests.get(link)
        response.raise_for_status()
        return response.content
    except(requests.RequestException, ValueError) as e:
        print(f'Unable to access the network\n{e}')
        return False