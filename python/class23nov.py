import requests
from bs4 import BeautifulSoup
r=requests.get('https://www.tutorialspoint.com/python/index.htm')
s=BeautifulSoup(r.content,'html.parser')
ATAGS=s.find_all('a')
