# Example to API from https://www.upcitemdb.com
# https://www.upcitemdb.com/api/explorer#!/lookup/get_trial_lookup
import requests
import json
# Get response from Barcode: 0012993441012
baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
#parameters = {'upc': '012993441012'}
parameters = {'upc': '073366118238'}

response = requests.get(baseUrl, params=parameters)
print(response.url)
content = response.content
info = json.loads(content)
item = info['items']
itemInfo = item[0]
title = itemInfo['title']
brand = itemInfo['brand']
print(title)
print(brand)
