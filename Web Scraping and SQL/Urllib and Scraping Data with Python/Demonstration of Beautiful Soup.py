# Importing Libraries
import requests
from bs4 import BeautifulSoup

# Sending Request
hdr = {"User-Agent": "Mozilla/5.0"}
r = requests.get("https://www.goodreads.com/", headers=hdr)
r.status_code # status code 200 defines Success - OK

r = requests.get("https://www.goodreads.com/")
r.status_code

# Parsing the data
book_soup = BeautifulSoup(r.content, "html.parser")
categories=book_soup.find_all("a", attrs={'class': 'gr-hyperlink'})

# Organising the data
txt_categories=[]
for tag in categories:
    if 'genres' in tag.get('href'):
        txt_categories.append(tag.string)

# Printing the data
for category in txt_categories:
    print(category)
