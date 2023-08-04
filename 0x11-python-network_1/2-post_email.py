#!/usr/bin/python3
"""
python script that takes URL and email and displays response of POST function
"""
from urllib import request, parse
import sys


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script_name.py [URL] [email]")
        sys.exit(1)

    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = request.Request(sys.argv[1], data)

    try:
        with request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except request.URLError as e:
        print("An error occurred while making the request:", str(e))
