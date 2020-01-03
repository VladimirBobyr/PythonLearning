# Requirements:
# Modules: requests, lxml, beautifulsoup4
import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'
'''response = requests.get(url)
file1 = open('response_file.html','+w',encoding='utf8')
file1.write(response.text)

soup = BeautifulSoup(response.text, 'lxml')
file2 = open('soup_file.html','+w',encoding='utf8')
file2.write(soup.quote)
file1.close()
file2.close()
'''

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')
for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a', class_='tag')
    for quoteTag in quoteTags:
        print(quoteTag.text)
