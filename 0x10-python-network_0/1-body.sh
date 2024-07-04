#!/bin/bash
# thais script takes in a URL and sends a request to that URL and display size
response=$(curl -s -w "%{http_code}" "$1")
body=$(echo "$response" | sed '$d')
status_code=$(echo "$response" | tail -n1)
