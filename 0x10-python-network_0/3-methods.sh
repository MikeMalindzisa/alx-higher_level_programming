#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept

# Usage message
usage() {
    echo "Usage: $0 <URL>"
    exit 1
}

# Check if URL is provided
if [ $# -ne 1 ]; then
    usage
fi

# Send OPTIONS request to the URL and display allowed methods
curl -s -i -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f2-

