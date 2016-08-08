__author__ = 'Zane'
import requests

r = requests.get('http://www.baidu.com')
print type(r)
print r.status_code
print r.cookies
print r.encoding
#print r.text

datas = {'key1' : 'value1', 'key2' : 'value2'}
r2 = requests.post("http://httpbin.org/post", data=datas)
print r2.text

file = {'file' : open('interfacedoc.txt', 'rb')}
r3 = requests.post('http://httpbin.org/post', files=file)
print r3.text

cookies = {'cookies_are' : 'working'}
r4 = requests.get('http://httpbin.org/cookies', cookies = cookies)
print r4.text

r5 = requests.get('https://www.github.com', verify=True)
print  r5.text

r6 = requests.get('https://kyfw.12306.cn/otn/', verify=False)
print r6.text

