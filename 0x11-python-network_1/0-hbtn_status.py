#!/usr/bin/python3

from urllib.request import urlopen


with urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read(100)

print('Body response:')
print('\t- type: {}'.format(body.__class__))
print('\t- content: {}'.format(body))
print('\t- utf8 content: {}'.format(body.decode()))
