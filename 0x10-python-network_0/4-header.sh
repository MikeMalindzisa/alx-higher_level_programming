#!/bin/bash
# Takes in a URL as an argument, sends a GET request to the URL with a custom header X-School-User-Id set to 98, and displays the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
