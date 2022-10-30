#!/usr/bin/python3

"""Python script that takes 2 arguments in order to solve this challenge.
# The first argument will be the repository name
# The second argument will be the owner name
# You must use the packages requests and sys
# You are not allowed to import packages other than requests and sys
# You don’t need to check arguments passed to the script (number or type)"""

from sys import argv
import requests

if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
            argv[2], argv[1])
    r = requests.get(url)
    rJson = r.json()

    for i in range(10):
        sha = rJson[i]['sha']
        name = rJson[i]['commit']['author']['name']
        print('{}: {}'.format(sha, name))
