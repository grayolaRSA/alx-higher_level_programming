#!/bin/bash
# Script that sends POST request to URL with data, and displays the body of the response
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
