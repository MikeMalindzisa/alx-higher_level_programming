#!/bin/bash
# Takes in a URL, sends a request to that URL using curl, and displays the size of the body of the response in bytes

# Check if URL is provided
if [ $# -ne 1 ]; then
    usage
fi

# Send request and display content length
curl -sI "$1" | awk '/Content-Length/ {print $2}'

