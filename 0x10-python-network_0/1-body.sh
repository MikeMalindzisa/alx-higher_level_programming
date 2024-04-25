#!/bin/bash
# Takes in a URL, sends a GET request to the URL using curl, and displays the body of the response if the status code is 200

# Usage message
usage() {
    echo "Usage: $0 <URL>"
    exit 1
}

# Check if URL is provided
if [ $# -ne 1 ]; then
    usage
fi

# Send GET request and display body of response if status code is 200
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")
if [ "$response" -eq 200 ]; then
    curl -s "$1"
fi

