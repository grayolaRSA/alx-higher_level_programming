#!/bin/bash
# script sends requests to URL and displays response
curl -s -I "$1" | grep "Content-Length:" | cut -d " " -f 2
