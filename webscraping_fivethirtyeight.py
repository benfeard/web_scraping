'''
Today's FiveThirtyEight Headlines
Thu Oct 8 2020
by Benfeard Williams
'''

#libraries
import requests
from bs4 import BeautifulSoup

#website and scrape content
URL = "https://www.fivethirtyeight.com"
r1 = requests.get(URL)
coverpage = r1.content

#make soup
soup1 = BeautifulSoup(coverpage, 'html.parser')

#my owninvestigation shows bigger headlines with h2 
#and smaller headlines with h3 on the main page
coverpage_news1 = soup1.find_all('h2', class_='article-title entry-title')
coverpage_news2 = soup1.find_all('h3', class_='article-title entry-title')

#let's make a list of headlines
headlines = []

for soup in [coverpage_news1, coverpage_news2]:
    for entry in soup:
        headlines.append(entry.get_text())

#print to screen in a readable format
for index in range(len(headlines)):
    article = headlines[index]
    print str(index + 1) + " - " + article.replace('\n','')
