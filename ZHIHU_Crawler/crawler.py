# -*- coding: utf-8 -*-
# encoding:utf-8
__author__ = 'Zane'

import requests
from lxml import etree

#爬取的主要基类
class Zhihu_crawler():

    def __init__(self, url):
        self.url = url
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
                        , "Host":"www.zhihu.com"
                        , "Refer":"www.zhihu.com"}

        #cookie
        self.cookies={"z_c0":'"Mi4wQUJES1hxTE1SUWdBWUVET3JKT2pDUmNBQUFCaEFsVk5TM1BXVndBME9mLXQ4STM2bWFlM1JJOXF0c1pld0tCbTh3|1471179482|287cc1b9a28f7d338fd89d6771cd4590b764cce9"',
                "unlock_ticket":'QUZDQUp3czV3QWtYQUFBQVlRSlZUZnBxQ2xmSWNXX3NuVXo3SVJleUM5Uy1BLUpEdXJEcEpBPT0',
                "login":'"ZTEwOGU2NjhiNWE5NGQyOWE4ODY0YjMzMTg2MGUyZjU=|1471080002|4ebda99342dafce4f0fa2f9873b1f9aa152db9ee"',
                "n_c":"1",
                "q_c1":"3b3a3dccecf1499ea32a0b2da9be35ec|1470149980000|1445741536000",
                "l_cap_id":'"OGRmYmZhNWUxN2MwNDE4MWI4MDE5MzIyZDQwZjE5NDE=|1471080000|a826857321160d83eee323a9ab1dc119c46ec95d"',
                "d_c0":'"AGBAzqyTowmPTpYh7UrYZSjcr43LFX006Tw=|1461248461"',
                "cap_id":'"MTNhNDQxODNmYjQ5NGE1YmIzM2Y5NmMzNDI5YzZkYTA=|1471080000|88bbcb97639ddfd83e41a37d73c1a6fe3240027b"'}

    def send_request(self):
        #关注者的url
        followees_url = self.url + '/followees'
        #发起请求
        try:
            #避免Https的证书验证
            r = requests.get(followees_url, cookies = self.cookies, headers = self.headers, verify = False)
        except:
            print "requests error! " + r.status_code
            return

        content = r.text
        if r.status_code == 200:
            self.parse_users_content(content)
            print "requests success!"

    #判断是否数据存在
    def judge_data_have(self, name, datas):
        if datas:
            print datas[0]
            return datas[0]
        else:
            print name + " not exist!"
            return

    #解析数据
    def parse_users_content(self, html_source):
        #初始化我们需要的信息变量
        self.user_name=''
        self.user_gender=''
        self.user_location=''
        self.user_followees=''
        self.user_followers=''
        self.user_be_agreed=''
        self.user_be_thanked=''
        self.user_education_school=''
        self.user_education_subject=''
        self.user_employment=''
        self.user_employment_extra=''
        self.user_intro=''

        tree = etree.HTML(html_source)

        self.user_name = self.judge_data_have("姓名", tree.xpath('//a[@class = "name"]/text()'))
        self.user_location = self.judge_data_have("位置", tree.xpath('//span[@class = "location item"]/@title'))
        self.user_gender = self.judge_data_have("性别", tree.xpath('//span[@class = "item gender"]/i/@class'))
        if 'male' in self.user_gender and self.user_gender:
            self.user_gender = 'male'
        elif 'female' in self.user_gender and self.user_gender:
            self.user_gender = 'female'

        self.user_followees = tree.xpath('//div[@class = "zu-main-sidebar"]//strong/text()')[0]
        self.user_followers = tree.xpath('//div[@class = "zu-main-sidebar"]//strong/text()')[1]
        self.user_be_agreed = tree.xpath('//div[@class = "zm-profile-header-info-list"]//strong/text()')[0]
        self.user_be_thanked = tree.xpath('//div[@class = "zm-profile-header-info-list"]//strong/text()')[1]
        self.user_education_school = self.judge_data_have("学校", tree.xpath('//span[@class = "education item"]/a/@title'))
        self.user_education_subject = self.judge_data_have("学科", tree.xpath('//span[@class = "education-extra item"]/a/@title'))
        self.user_employment = self.judge_data_have("公司", tree.xpath('//span[@class = "employment item"]/@title'))
        self.user_employment_extra = self.judge_data_have("公司", tree.xpath('//span[@class = "position item"]/@title'))
        self.user_intro = self.judge_data_have("简介", tree.xpath('//div[@class = "bio ellipsis"]/@title'))

        #打印最终信息
    def print_data_out(self):
        print "*"*60
        print "用户名:%s".decode('utf-8') % self.user_name
        print "用户性别:%s".decode('utf-8') % self.user_gender
        print "用户地址:%s".decode('utf-8') % self.user_location
        print "被同意:%s".decode('utf-8') % self.user_be_agreed
        print "被感谢:%s".decode('utf-8') % self.user_be_thanked
        print "被关注:%s".decode('utf-8') % self.user_followers
        print "关注了:%s".decode('utf-8') % self.user_followees
        print "工作:%s/%s".decode('utf-8') % (self.user_employment,self.user_employment_extra)
        print "教育:%s/%s".decode('utf-8') % (self.user_education_school,self.user_education_subject)
        print "用户信息:%s".decode('utf-8') % self.user_intro
        print "*"*60



