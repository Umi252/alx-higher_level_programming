#!/bin/bash
# Script to display the body of a 200 status code response

[ -z "$1" ] && echo "Please provide a URL as an argument." && exit 1
curl -s -o response.txt -w "%{http_code}" "$1" --output - | awk '/^200$/{body=1;next} body{print}'
