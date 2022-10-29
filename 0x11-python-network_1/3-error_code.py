#!/usr/bin/python3

"""Script takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)"""

from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == '__main__':
    try:
        with urlopen(argv[1], timeout=10) as response:
            print(response.read().decode())
    except HTTPError as error:
        print("Error code:", error.status)
