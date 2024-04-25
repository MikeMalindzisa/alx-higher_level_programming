#!/bin/bash
# Sends a DELETE request to the URL passed as the first argument and displays the body of the response

# Usage message
usage() {
    echo "Usage: $0 <URL>"
    exit 1
}

# Check if URL is provided
if [ $# -ne 1 ]; then
    usage
fi

# Send DELETE request and display body of response
curl -s -X DELETE "$1"

