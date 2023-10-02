#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
"""
import requests
from sys import argv


def main(argv):
    """
    displays the value of the X-Request-Id variable
    """
    url = argv[1]
    r = requests.get(url)
    headers = r.headers.get('X-Request-Id')
    print(headers)

if __name__ == "__main__":
    main(argv)
