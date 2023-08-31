import requests

client = requests.get("https://www.google.com")
print(client.cookies)
print(client.cookies.get_dict())
