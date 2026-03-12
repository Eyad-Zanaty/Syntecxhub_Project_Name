import requests
import json
import sqlite3
import csv
from datetime import datetime

api_key= '2c56649e79254a23b5d93a420c996232';

data= requests.get(fr'https://newsapi.org/v2/everything?q=gold&apiKey={api_key}').json()
# Deduplicate articles by URL
seen_urls = set()
unique_articles = []
for article in data.get('articles', []):
    if article['url'] not in seen_urls:
        seen_urls.add(article['url'])
        unique_articles.append(article)

# Save to SQLite
conn = sqlite3.connect('week04/news.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS articles
                  (id INTEGER PRIMARY KEY, title TEXT, url TEXT UNIQUE, source TEXT, published_at TEXT)''')

for article in unique_articles:
    try:
        cursor.execute('INSERT INTO articles (title, url, source, published_at) VALUES (?, ?, ?, ?)',
                      (article['title'], article['url'], article['source']['name'], article['publishedAt']))
    except sqlite3.IntegrityError:
        pass
conn.commit()
conn.close()

# Save to JSON
with open('week04/news.json', 'w', encoding='utf-8') as f:
    json.dump(unique_articles, f, indent=2)

# Export to CSV
with open('week04/news.csv', 'w', newline='', encoding='utf-8') as f:
    if unique_articles:
        writer = csv.DictWriter(f, fieldnames=['title', 'url', 'source', 'publishedAt'])
        writer.writeheader()
        for article in unique_articles:
            writer.writerow({'title': article['title'], 'url': article['url'], 
                           'source': article['source']['name'], 'publishedAt': article['publishedAt']})
print(data)