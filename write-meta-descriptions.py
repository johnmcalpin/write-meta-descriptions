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
    description_tag = soup.find('meta', {'name': 'description'})
    if description_tag:
        description = description_tag.get('content')
        # 3) writes a meta description for each URL with a maximum character count of 155 characters
        if len(description) >= 135 and len(description) <= 160:
            results.append({
                'url': url,
                'description': description
            })
    else:
        results.append({
                'url': url,
                'description': ' '
        })
# 4) exports the results to a csv file
with open('results.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['url', 'description'])
    writer.writeheader()
    writer.writerows(results)
