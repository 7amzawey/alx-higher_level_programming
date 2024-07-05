#!/bin/bash
# sends a json post request to a url passed as the first argument
curl -s -X Post -H "Content-Type: application/json" -d @"$2" "$1"
