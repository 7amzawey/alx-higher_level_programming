#!/bin/bash
# this script sends a request to a url and diplays only the status code
curl -s -o dev/null -w "%{http_code}" "$1"
