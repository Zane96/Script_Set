import urllib2
import cookielib

file_name = "cookie.txt"

cookie = cookielib.MozillaCookieJar(file_name)
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

response = opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True, ignore_expires=True)
for item in cookie:
    print item.name
    print item.value
