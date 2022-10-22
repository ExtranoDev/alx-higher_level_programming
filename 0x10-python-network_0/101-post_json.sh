#!/bin/bash
# send a POST request with the contents of a file
curl "$1" -sX POST -d @"$2" -H "Content-Type: application/json"
