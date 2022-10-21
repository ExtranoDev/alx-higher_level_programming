#!/bin/bash
# displays the size of the body of the response
curl -s --head "$1" | grep "Content-Length" | cut -c 17-
