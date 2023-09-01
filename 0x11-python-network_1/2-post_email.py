#!/usr/bin/python3

"""POST an email #0"""

from urllib import request, parse
import sys

if __name__ == "__main__":
    data = parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    with request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode('utf-8'))
