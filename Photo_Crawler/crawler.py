# -*- coding: utf-8 -*-
# encoding:utf-8
__author__ = 'Zane'

import requests
import xml.etree.ElementTree as ET

class photo_crawler():

    def __init__(self, page):

        self.page = page
        self.request_payload = '<?xml version="1.0" encoding="utf-8"?><BxMessage><AppId>BxAPI</AppId><Type>1</Type><Action>getPhotoList</Action><Data><words>nonumber</words><pageindex>'+ str(page) + '</pageindex><pagesize>300</pagesize><searchmode>nonumber</searchmode><positionid>0</positionid></Data></BxMessage>'
        self.url = "http://www.runff.com/html/photo/s1166.html?isbxapimode=true"
        self.origin_data = 'origin/origin' + str(self.page) + '.txt'

        #构建请求头
        self.headers = {"Accept": "text/plain, */*; q=0.01"
           ,    "Accept-Encoding": "gzip, deflate"
           ,    "Content-Type": "text/plain"
           ,    "Host": "www.runff.com"
           ,    "Cache-Control": "max-age=0"
           ,    "Connection": "keep-alive"
           ,    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4"
           ,    "Content-Length": "267"
           ,    "Origin": "http://www.runff.com"
           ,    "Referer": "http://www.runff.com/html/photo/s1166.html"
           ,    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"
           ,    "X-Requested-With": "XMLHttpRequest"}

        #构建cookie
        self.cookies = {"ASP.NET_SessionId": "du5h3owthwqbwsc2c1henmch"
           ,    "__cfduid": "d949d5b3f6b954f0b3b6915a93e037bf31479377209"
           ,    "Hm_lvt_3de671d246685f9f53214b84803799b6": "1479377203"
           ,    "Hm_lpvt_3de671d246685f9f53214b84803799b6": "1479382996"
           ,    "Hm_lvt_26fad0fa647fab8971d4c110d92f6535": "1479377203"
           ,    "Hm_lpvt_26fad0fa647fab8971d4c110d92f6535": "1479382996"
           ,    "SERVERID": "ab1dba5cfcebe779c05894fcd320f4c0|1479383627|1479382318"}

    #发送请求,将所有229页的数据全部写入
    def send_request(self):
        r = requests.post(self.url, data=self.request_payload, headers=self.headers, cookies=self.cookies)
        print(r.text)
        try:
            r.raise_for_status()
        except requests.HTTPError as e:
            print e.message + ' HttpError'
        except requests.ConnectionError as e:
            print e.message

        if r.status_code == requests.codes.ok:
            self.write_origin_data(r)
            print "requests success!"


    #写入原始数据
    def write_origin_data(self, r):
        with open(self.origin_data, 'w') as f:
            #前面有一块乱码。。去除掉
            f.write(r.text[r.text.find('<'):])
        self.parse_xml_data()

    #解析原始数据
    def parse_xml_data(self):
        tree = ET.parse(self.origin_data)
        list = ''
        for elem in tree.iter(tag='list'):
            list = elem.text
        big_image_urls = list.split(',')
        self.write_bigimage_data(big_image_urls)


    #写入最终的大图imageurl
    def write_bigimage_data(self, big_image_urls):
        n = 1
        str_big_urls = ''
        while n < len(big_image_urls) - 3:
            big_image_url = big_image_urls[n]
            str_big_urls += big_image_url[15:len(big_image_url)-1] + '\n'
            n = n + 4

        big_image_dir = 'bigimages/page' + str(self.page) + '.txt'
        #写入文件
        with open(big_image_dir, 'w') as f:
            f.write(str_big_urls)