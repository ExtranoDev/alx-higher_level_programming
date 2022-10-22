#!/bin/bash
# sends request to url and get response code only
curl "$1" -so /dev/null --write-out "%{http_code}"
