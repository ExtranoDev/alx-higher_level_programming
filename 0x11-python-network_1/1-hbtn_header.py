#!/usr/bin/python3

""" script that takes in a URL,
    sends a request to the URL and
    displays the value of the X-Request-Id header variable
"""
from urllib.request import urlopen
import sys

url = sys.argv[1]
with urlopen(url) as response:
    print(response.headers.get('X-Request-Id'))
