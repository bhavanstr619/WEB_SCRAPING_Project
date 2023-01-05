import requests
from bs4 import BeautifulSoup
try:
    r=requests.get("https://en.m.wikipedia.org/wiki/History_of_Google")
    soup=BeautifulSoup(r.content,'html.parser')
    p=soup.find('title').text
    p1=soup.find(class_='mw-body-content mw-content-ltr').text
    print(p)
    print(p1)
except Exception as e:
    print(e)