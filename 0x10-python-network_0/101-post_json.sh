#!/bin/bash
# Sends a JSON POST request to a URL passed as the first argument, using the contents of a file as the request body
# Displays the body of the response

# Usage message
usage() {
    echo "Usage: $0 <URL> <JSON_FILE>"
    exit 1
}

# Check if both URL and JSON file are provided
if [ $# -ne 2 ]; then
    usage
fi

# Check if the JSON file is valid JSON
if ! jq '.' "$2" >/dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

# Send POST request with JSON file as the body and display the response body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1" -L
