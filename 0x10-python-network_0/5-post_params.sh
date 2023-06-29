#!/bin/bash
# script that takes URL request and displays body
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
