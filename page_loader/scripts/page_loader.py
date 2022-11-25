from page_loader import download
from page_loader.cli_parser import parse_args


def main():
    args = parse_args()
    print(args.output, args.link)
    print(download(args.output, args.link))
