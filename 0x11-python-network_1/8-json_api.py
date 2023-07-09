#!/usr/bin/python3
"""
python script that sends URL request with letter as parameter
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        dic = sys.argv[1]
    else:
        dic = ""

        payl = {'q': dic}

        r = requests.post('http://0.0.0.0:5000/search_user', data=payl)

        try:
            data = r.json()
            if not json_o:
                print("No result")
            else:
                print("[{}] {}".format(json_o.get('id'), json_o.get('name')))
        except ValueError:
            print("Not a valid JSON")
