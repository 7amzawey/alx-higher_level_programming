#!/bin/bash
# thais script takes in a URL and sends a request to that URL and display body
curl -s -o /dev/null -w "%{http_code}" "$1"
