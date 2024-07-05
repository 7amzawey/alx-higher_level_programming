#!/bin/bash
# send a post request to the URL and displays the body of the response
curl -s -X POST -H "email: test@gmail.com" -H "subject: I will always be here for PLD" "$1"
