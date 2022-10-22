#!/bin/bash
# sends a GET request to the URL with a header variable
curl -sX GET -H "X-School-User-Id: 98" "$1"
