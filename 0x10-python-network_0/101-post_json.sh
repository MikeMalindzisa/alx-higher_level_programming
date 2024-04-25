#!/bin/bash
# Sends a JSON POST request to a URL passed as the first argument, using the contents of a file as the request body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1" -L
