#!/usr/bin/python3
"""
python script that sends URL request and displays requested header variable
"""
import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.headers['X-Request-Id'])
    except ValueError:
        pass
