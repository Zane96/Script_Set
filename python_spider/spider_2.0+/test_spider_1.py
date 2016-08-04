import urllib2
from bs4 import BeautifulSoup

__author__ = 'Zane'

page = 1
url = "http://www.qiushibaike.com/hot/page/" + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent':user_agent}

try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    divs = soup.select('div[class="content"]')
    laughs = soup.select('span[class="stats-vote"]')
    comments = soup.select('a[class="qiushi_comments"]')

    for comment in comments:
        if comment != None:
            print comment.i.string, 'comment'
    for laugh in laughs:
        print laugh.i.string, 'laugh'
    for div in divs:
        if div != None:
            print div.string
except urllib2.URLError as e:
    if hasattr(e, 'code'):
        print e.code
    if hasattr(e, 'reason'):
        print e.reason