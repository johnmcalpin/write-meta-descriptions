import csv
import requests
from bs4 import BeautifulSoup

# 1) imports a list of URLs from a txt file
with open('/content/drive/MyDrive/urls.txt') as f:
    urls = [line.strip() for line in f]

results = []

# 2) analyzes the content on each URL
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 3) writes a meta description for each URL with a maximum character count of 155 characters
    description = soup.find('meta', {'name': 'description'}).get('content')
    if len(description) > 155:
        description = description[:152] + '...'

    results.append({
        'url': url,
        'description': description
    })

# 4) exports the results to a csv file
with open('results.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['url', 'description'])
    writer.writeheader()
    writer.writerows(results)
