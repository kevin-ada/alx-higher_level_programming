#!/usr/bin/python3

"""" POST an email #1"""
import requests
import sys

if __name__ == '__main__':
    email = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], data=email)
    print(response.text)


