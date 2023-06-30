#!/usr/bin/python3
"""
Python script that sends URL request and displays X-request variable
"""
import requests
import sys


if __name__ == "__main__":
    try:
        r = requests.get(sys.argv[1])
        print(r.headers['X-Request-Id'])
    except ValueError:
        pass
