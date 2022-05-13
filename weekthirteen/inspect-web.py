#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup

response = requests.get("https://notpurple.com")
soup = BeautifulSoup(response.text, 'html.parser')
title = str(soup.find('title'))
links = str(soup.findAll('a'))
sliced_title = title[7:24:]
sliced_links1 = links[10:18:]
sliced_links2 = links[40:50:]
print(title)
print(links)
print('')
print("Slicing Title And Links to Look Nice")
print('')
print(sliced_title)
print(sliced_links1)
print(sliced_links2)