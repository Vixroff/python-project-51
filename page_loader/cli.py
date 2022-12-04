import argparse


def parse_args():
    """CLI arguments parser"""
    parser = argparse.ArgumentParser(
        prog="page-loader",
        description="Download HTML page from a link and save it into entered directory")
    parser.add_argument(
        'link',
        help="Link where HTML would be downloaded")
    parser.add_argument(
        '-o', '--output',
        help="Directory where HTML page would be saved\ndefault is current dir",
        default='current')
    args = parser.parse_args()
    return args
