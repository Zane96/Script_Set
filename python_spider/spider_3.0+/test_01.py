import urllib.request
url = "http://www.adastaybrave.com"
response = urllib.request.urlopen(url)
html = response.read()
print (html)