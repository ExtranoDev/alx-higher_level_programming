#!/bin/bash
# sends request to url and get response code only
curl "$1" -os /dev/null --write-out %{http_code}
