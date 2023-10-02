#!/usr/bin/python3
"""
Sends a requestand displays the body of the response.
"""
import requests
from sys import argv


def main(argv):
    """
    Method that handles urllib.error.HTTPError exceptions and
    """
    url = argv[1]
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))


if __name__ == "__main__":
    main(argv)
