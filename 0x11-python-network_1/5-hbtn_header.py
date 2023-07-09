#!/usr/bin/python3
"""
python script that sends URL request and displays requested header variable
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if 'X-Request-Id' in r.headers:
        print(r.headers['X-Request-Id'])
    else:
        exit(1)
