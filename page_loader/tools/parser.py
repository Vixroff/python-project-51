import requests


from page_loader.log import logger


def parse(url):
    """
    This function makes request to url and returns html code or False if error there
    """
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        logger.info(f'GET DATA: {url}')
        return response.content
    except requests.RequestException as e:
        logger.error(f'ERROR: {e} - Unable to access the network: {url}')
        raise e(f'ERROR: {e} - Unable to access the network: {url}')
