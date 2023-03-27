import ssl
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

gcontext = ssl.SSLContext()

url = "https://opensea.io/ja/collection/nakamigos"
req = Request(url=url, headers={"User-Agent": "Mozilla/5.0"})
webpage = urlopen(req, context=gcontext).read()

# for line in webpage:
#     print(line.decode('utf-8'))

soup = BeautifulSoup(webpage, features="html.parser")
print(soup)
