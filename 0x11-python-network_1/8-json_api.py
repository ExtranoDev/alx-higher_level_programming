#!/usr/bin/python3

"""Script takes in a letter and sends a POST request to url
with the letter as a parameter"""

import requests
from sys import argv

if __name__ == '__main__':
    if argv[1]:
        par = {'q': argv[1]}
    else:
        {'q': ''}
    r = requests.post('http://0.0.0.0:5000/search_user', par)
    resJson = r.json()
    if resJson == {}:
        output = 'No result'
    elif type(resJson) != dict:
        output = 'Not a valid JSON'
    else:
        output = '[' + str(resJson['id']) + '] ' + resJson['name']
    print(output)
