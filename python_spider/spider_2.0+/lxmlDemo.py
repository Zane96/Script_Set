from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-4"><a id="123 456" href="link5.html">fifth item</a>
     </ul>
 </div>
'''

html = etree.HTML(text)
print etree.tostring(html)

result = html.xpath('//li')
print result
result = html.xpath('//li/@class')
print result
result = html.xpath('//li/a[@href = "link4.html"]/text()')[0]
print result
result = html.xpath('//li//span')
print result
print html.xpath('//li[last()]/a/@href')[0]
print html.xpath('//li[last() - 1]/a')[0].text
print html.xpath('//*[@class = "item-0"]/a')[0].text
print html.xpath('//li[@class="item-4"]/a/@id')