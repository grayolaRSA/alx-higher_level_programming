#!/usr/bin/python3
"""
python script that gets alx webpage using requests module
"""
import requests


if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    t = r.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(t), t))
