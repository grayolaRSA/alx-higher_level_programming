#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
and returns body of response
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
