#!/usr/bin/python3
"""What's my status? #1"""
import requests
if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.content.decode('utf-8')))
