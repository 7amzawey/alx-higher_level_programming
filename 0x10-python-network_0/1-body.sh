#!/bin/bash
# thais script takes in a URL and sends a request to that URL and display body
curl -s -o /dev/null -w "%{http_code}" "$1" | { read http_status; if [ "$http_status" -eq 200 ]; then curl -sL "$1"; fi; }
