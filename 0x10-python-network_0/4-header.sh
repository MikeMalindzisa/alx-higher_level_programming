#!/bin/bash
# Takes in a URL as an argument, sends a GET request to the URL with a custom header X-School-User-Id set to 98, and displays the body of the response

# Usage message
usage() {
    echo "Usage: $0 <URL>"
    exit 1
}

# Check if URL is provided
if [ $# -ne 1 ]; then
    usage
fi

# Send GET request with custom header and display body of response
curl -s -H "X-School-User-Id: 98" "$1"

