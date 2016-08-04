#coding=utf-8
__author__ = 'Zane'
import urllib2
from bs4 import BeautifulSoup, Tag
import re

#处理页面标签类
class Tool:
    #把段落开头换为\n加空两格
    replacePara = re.compile('\s{3,8}')
    def replace(self,x):

        x = re.sub(self.replacePara,"\n",x)

        #strip()将前后多余内容删除
        return x.strip()

class BDTB:
    def __init__(self, base_url, see_lz):
        self.base_url = base_url
        self.see_lz = "?see_lz=" + str(see_lz)
        self.tool = Tool()

    def getPage(self, page_num):
        url = self.base_url + self.see_lz + "&pn=" + str(page_num)
        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            html = response.read()
            #soup = BeautifulSoup(html, 'html.parser')
            #print soup.prettify()
            return html
        except urllib2.HTTPError as e:
            if hasattr(e, 'code'):
                print e.code
            if hasattr(e, 'reason'):
                print e.reason

    def getTitle(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        print '标题:', soup.find("h3", class_="core_title_txt pull-left text-overflow ")['title']

    def getPages(self, html):
        #def has_class_no_style(tag):
            #return tag.has_attr('class') and not tag.has_attr('style')
        soup = BeautifulSoup(html, 'html.parser')
        spans = soup.find_all("span", class_='red')
        print '页数:', spans[1].string
        return spans[1].string

    def getContent(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        divs = soup('div', {'class':'d_post_content j_d_post_content '})
        content = ''
        for div in divs:
            for child in div.descendants:
                if type(child) != Tag:
                    content = content + child

        print self.tool.replace(content)


if __name__ == '__main__':
    baseURL = 'http://tieba.baidu.com/p/3138733512'
    bdtb = BDTB(baseURL, 1)
    for i in range(1, 5):
        html = bdtb.getPage(i)
        bdtb.getTitle(html)
        bdtb.getPages(html)
        bdtb.getContent(html)

