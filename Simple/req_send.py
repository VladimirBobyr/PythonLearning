import requests

url = 'https://www.w3schools.com/python/demopage.php'
myobj = {'somekey': 'somevalue'}

x = requests.post(url, data = myobj)

print(x.text)

x = requests.get('https://w3schools.com')
print(x.status_code)