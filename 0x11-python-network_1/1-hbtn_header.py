#!/usr/bin/python3

from urllib.request import urlopen
import sys


url = sys.argv[1]
with urlopen(url) as response:
    print(response.headers.get('X-Request-Id'))
