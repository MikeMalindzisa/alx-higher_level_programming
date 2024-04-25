#!/bin/bash
# Sends a request to a URL passed as an argument and displays only the status code of the response

# Usage message
usage() {
    echo "Usage: $0 <URL>"
    exit 1
}

# Check if URL is provided
if [ $# -ne 1 ]; then
    usage
fi

# Send request and display only the status code
curl -s -o /dev/null -w "%{http_code}" "$1"

