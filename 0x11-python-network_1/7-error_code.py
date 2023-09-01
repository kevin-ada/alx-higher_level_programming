#!/usr/bin/python3
"""" Error code #1"""
import sys

import requests

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.content)
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
