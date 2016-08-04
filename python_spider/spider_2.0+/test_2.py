import urllib2

req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    print urllib2.urlopen(req).read()
except urllib2.HTTPError as e:
    print e.reason
    print e.code
except urllib2.URLError as e:
    print e.reason
else:
    print 'OK'
