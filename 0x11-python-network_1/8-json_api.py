#!/usr/bin/python3

"""Script takes in a letter and sends a POST request to url
with the letter as a parameter"""

import requests
from sys import argv

if __name__ == '__main__':
    par = {'q': ''}
    if len(argv[1]) > 1:
        par = {'q': argv[1]}
        r = requests.post('http://0.0.0.0:5000/search_user', par)
        if r.headers.get('Content-Type') == 'application/json':
            resJson = r.json()
            if resJson == {}:
                print('No result')
            else:
                print("[{}] {}".format(resJson['id'], resJson['name']))
        else:
            print('Not a valid JSON')
    else:
        print('No result')
