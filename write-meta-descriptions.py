!pip install sumy
from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
from sumy.summarizers.lsa import LsaSummarizer
import csv

#1) imports a list of URLs from a txt file
with open('urls.txt') as f:
    urls = [line.strip() for line in f]

results = []

# 2) analyzes the content on each URL
for url in urls:
    parser = HtmlParser.from_url(url, Tokenizer("english"))
    stemmer = Stemmer("english")
    summarizer = LsaSummarizer(stemmer)
    summarizer.stop_words = get_stop_words("english")
    description = summarizer(parser.document, 3)
    description = " ".join([sentence._text for sentence in description])
    if len(description) > 155:
        description = description[:152] + '...'
    results.append({
        'url': url,
        'description': description
    })

# 4) exports the results to a csv file
with open('results.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['url','description'])
    writer.writeheader()
    writer.writerows(results)
