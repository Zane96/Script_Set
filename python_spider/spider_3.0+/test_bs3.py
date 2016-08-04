import urllib.request
import urllib.error

req = urllib.request.Request('http://www.assda123.com')

try:
    urllib.request.urlopen(req)
except urllib.error.URLError as error:
    print(error.reason)
