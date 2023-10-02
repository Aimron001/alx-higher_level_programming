#!/usr/bin/python3
"""
POST request with the email as a parameter
"""
import requests
from sys import argv


def main(argv):
    """
    Sends a POST request to the passed URL with the email as a parameter,
    """
    values = {'email': argv[2]}
    url = argv[1]
    r = requests.post(url, data=values)
    print(r.text)


if __name__ == "__main__":
    main(argv)
