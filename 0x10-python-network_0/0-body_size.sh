#!/bin/bash
# thais script takes in a URL and sends a request to that URL and display size
curl -s -o /dev/null -w '%{size_download}\n' "$1"
