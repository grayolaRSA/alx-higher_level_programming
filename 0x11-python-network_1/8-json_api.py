#!/usr/bin/python3
"""
python script that sends URL request with letter as parameter
"""
import requests
import sys


if __name__ == "__main__":
    data = {'q': ""}
    r = requests.post('http://0.0.0.0:5000/search_user', data)
    if data['q'] != "":
        try:
            data['q'] = sys.argv[1]
            json_o = r.json()
            if not json_o:
                print("No result")
            else:
                print("[{}] {}".format(json_o.get('id'), json_o.get('name')))
        except TypeError:
            print("Not a valid JSON")
        else:
            exit(1)
