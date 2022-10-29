#!/usr/bin/python3

"""script fetches url"""

import requests

r = requests.get('https://alx-intranet.hbtn.io/status')
print('Body response:')
print('\t- type:', r.text.__class__)
print('\t- content:', r.text)
