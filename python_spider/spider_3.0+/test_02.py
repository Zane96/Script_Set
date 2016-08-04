import urllib.request
response = urllib.request.urlopen("http://placekitten.com/500/600")
kitten_img = response.read()
with open('kitten_img.png', 'wb') as f:
    f.write(kitten_img)