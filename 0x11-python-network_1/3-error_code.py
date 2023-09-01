#!/usr/bin/python3
""""Error code #0"""

from urllib import request, error
import sys

with request.urlopen(sys.argv[1]) as response:
    try:
        print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
