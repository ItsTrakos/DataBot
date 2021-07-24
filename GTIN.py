#مكاتب
import requests
import secrets
import sys as n
import time as mm

req = requests.session()
head = {
'HOST': "www.instagram.com",
'KeepAlive' : 'True',
'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
'Cookie': 'cookie',
'Accept' : "*/*",
'ContentType' : "application/x-www-form-urlencoded",
"X-Requested-With" : "XMLHttpRequest",
"X-IG-App-ID": "936619743392459",
"X-Instagram-AJAX" : "missing",
"X-CSRFToken" : "missing",
"Accept-Language" : "en-US,en;q=0.9"
}
cookie = secrets.token_hex(8)*2
r = requests.Session()
#تارجيت
target = input('[+] Enter User : ')#تراكوس
url_id = f'https://www.instagram.com/{target}/?__a=1'
req_id = r.get(url_id,headers=head).json()
#الايدي
idd  = str(req_id['graphql']['user']['id'])
print(idd)
exit()
