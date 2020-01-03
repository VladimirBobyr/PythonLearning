# https://scrapingclub.com

from bs4 import BeautifulSoup
import requests
urlbasic = url = 'https://scrapingclub.com/exercise/list_basic/'
url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
for item in items:
    itemName = item.find('h4', class_='card-title').text.strip('\n')
    itemPrice = item.find('h5').text
    print('Name:%s Price: %s' % (itemName, itemPrice))

pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_='page-link')
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        x = link.get('href')
        urls.append(x)
print(urls)

for i in urls:
    newUrl = urlbasic + i
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    print('Page No:%s' % i)
    for item in items:
        itemName = item.find('h4', class_='card-title').text.strip('\n')
        itemPrice = item.find('h5').text
        print('Name:%s Price: %s' % (itemName, itemPrice))



