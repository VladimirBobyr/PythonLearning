from requests import session

payload = {
    'action': 'login',
    'username': 'zlogmein2009',
    'password': 'Q123456'
}

with session() as c:
    c.post('https://forum.oneclickchicks.com/secure-login.php', data=payload)
    response = c.get('https://forum.oneclickchicks.com/')
    print(response.headers)
    #print(response.text)