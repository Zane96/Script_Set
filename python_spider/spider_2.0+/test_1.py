import urllib2

req = urllib2.urlopen("http://www.baidu.com")
print req.read()