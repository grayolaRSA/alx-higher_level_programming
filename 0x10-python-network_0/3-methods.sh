#!/bin/bash
# script that takes in URL and displays all output of OPTION
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f -2
