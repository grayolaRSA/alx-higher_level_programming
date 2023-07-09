#!/usr/bin/python3
"""
Python script that sends POST request to URL with letter as parameter
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        data['q'] = sys.argv[1]
    else:
        data['q'] = ""

    r = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        json_o = r.json()
        if not json_o:
            print("No result")
        else:
            print("[{}] {}".format(json_o.get('id'), json_o.get('name')))
    except ValueError:
        print("Not a valid JSON")
