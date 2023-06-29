#!/bin/bash
# script that sends a GET request and displays body
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f -2
