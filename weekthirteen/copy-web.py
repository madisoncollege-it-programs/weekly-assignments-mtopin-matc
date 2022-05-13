#!/usr/bin/env python3
import requests

response = requests.get("https://notpurple.com")

with open("my_web_file.html", "w") as hFile:
    hFile.write(response.text)

