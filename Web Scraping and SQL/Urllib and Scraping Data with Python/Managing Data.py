import requests

r=requests.get("https://www.free-ebooks.net/best-books")
c=r.content

print(c)
