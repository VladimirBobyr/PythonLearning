import requests

http_proxy  = "http://54.37.73.112:3128"
https_proxy = "https://54.37.73.112:1080"
ftp_proxy   = "ftp://54.37.73.112:3128"

proxyDict = {
              "http": http_proxy,
              "https": https_proxy,
              "ftp": ftp_proxy
            }

url = 'http://imagefap.com'

r = requests.get(url, headers=headers, proxies=proxyDict)
