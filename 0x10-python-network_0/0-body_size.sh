#!/bin/bash

if [ -z "$1" ]; then
    echo "Please provide a URL as an argument."
    exit 1
fi

URL=$1
RESPONSE_SIZE=$(curl -s -o /dev/null -w "%{size_download}" "$URL")
echo "Response body size in bytes: $RESPONSE_SIZE"
