#학생1(김유빈) & 학생3(배수아)

!pip install cssselect
!pip install requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

import requests
import lxml.html
url='http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79'
r=requests.get(url)
r.status_code
root = lxml.html.fromstring(r.content)
titles=root.cssselect('div.title>a>strong')
titlelists=[]

for title in titles:
  titlelists.append(title.text.strip())
titlelists

#학생2(서지윤) & 학생3(배수아)
!pip install cssselect
!pip install requests
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

import requests
import lxml.html
url='http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79'
r=requests.get(url)
r.status_code
root = lxml.html.fromstring(r.content)
titles=root.cssselect('div.title>a>strong')
prices=root.cssselect('div.price>strong.book_price')

titlelists=[]
pricelists=[]

for i in range(len(titles)):
  titlelists.append(titles[i].text.strip())
  pricelists.append(prices[i].text.strip())

print(pricelists)
print(titlelists)

import pandas as pd
df=pd.DataFrame({"title":titlelists,
                 "price":pricelists})
df
