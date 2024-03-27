#!/bin/bash

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request to the URL and get the size of the response body in bytes
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
