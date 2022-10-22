#!/bin/bash
# sends a GET request to the URL with a header variable
curl -H "X-School-User-Id: 98" "$1"
