#!/bin/bash
# script that takes URL request and displays body
curl -s -X GET "$1" -H "X-School-User-Id: 98"
