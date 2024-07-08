#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept
curl -s -X OPTIONS -i 0.0.0.0:5000/catch_me | grep -i '^{' | sed -n 's/^{\s*//;s\s*}$//;p'
