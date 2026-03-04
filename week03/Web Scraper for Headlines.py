from bs4 import BeautifulSoup
import requests
import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

html_text= requests.get('https://www.foxnews.com/').text

soup= BeautifulSoup(html_text)

title= soup.find_all('h3', 'title')

data_list= []

for each in title:
    data= {
        'title': each.text.strip(),
        'href': each.a.get('href').strip() if each.a else None
    }
    data_list.append(data)

with open('scraped_data.json', 'w') as f:
    json.dump(data_list, f, indent=4)
