from pyquery import PyQuery as pq

p = pq('<p id="hello" class="hello"></p>')('p')
print p.append(' check out <a href="http://reddit.com/r/python"><span>reddit</span></a>')
print p.prepend('oh fuck')
d = pq('<div class="wrap"><div id="test"><a href="http://cuiqingcai.com">Germy</a></div></div>')
p.prependTo(d('#test'))
print p
print d
d.remove('a')
print d

doc = pq(filename='li.html')
lis = doc('li')
for li in lis.items():
    print li.html()

print lis.each(lambda e: e)