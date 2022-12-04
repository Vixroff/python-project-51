import sys
import requests


from page_loader import download
from page_loader.cli import parse_args


def main():
    args = parse_args()
    try:
        print(download(args.link, args.output))
    except requests.RequestException:
        print(f"Some issues with request to {args.link}")
        sys.exit(1)
    except IOError:
        print(f"Some issues with output {args.output}")
        sys.exit(1)
