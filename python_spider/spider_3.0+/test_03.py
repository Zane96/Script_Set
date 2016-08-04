import urllib.request
import json
import urllib.parse ##对data进行解析
import time

#data必须是byte(encode加码),json解析的必须是str(decode解码)

url = 'http://fanyi.youdao.com/translate?smartresu    lt=dict&smartresult=rule&smartresult=ugc&sessionFro    m=https://www.google.com/'

while True:
    content = input("你想翻译什么呢:")
    if content == 'q':
        break

    head = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'

    data = {"type":"AUTO", "i":content, "doctype":"json", "keyfrom":"fanyi.web",
        "xmlVersion":"1.8", "ue":"UTF-8", "typoResult":"true"}
    #解析请求表单
    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url, data)
    request.add_header('head', head)

    #生成完成的请求的response
    response = urllib.request.urlopen(request)

    html = response.read().decode('utf-8')
    target = json.loads(html)

    print("翻译结果是：%s" %(target['translateResult'][0][0]['tgt']))

    time.sleep(5)