#!/usr/bin/python3

""""Search API"""
import requests
import sys

if __name__ == "__main__":
    data = {"q": sys.argv[1] if len(sys.argv) > 1 else ""}
    request = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        json = request.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
