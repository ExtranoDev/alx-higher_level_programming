#!/bin/bash
# sends a POST request to the passed URL with data
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"