import requests

url = 'http://www.baidu.com'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0'}
req = requests.get(url, headers=headers).text
print(req)