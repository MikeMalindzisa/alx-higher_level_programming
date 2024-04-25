#!/bin/bash
# Takes in a URL, sends a POST request to the passed URL with specified parameters, and displays the body of the response

# Usage message
usage() {
    echo "Usage: $0 <URL>"
    exit 1
}

# Check if URL is provided
if [ $# -ne 1 ]; then
    usage
fi

# Send POST request with parameters and display body of response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"

