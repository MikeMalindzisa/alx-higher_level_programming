#!/bin/bash
# Takes in a URL, sends a GET request to the URL using curl, and displays the body of the response if the status code is 200
curl -sL "$1"
