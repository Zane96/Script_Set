# -*- coding: utf-8 -*-
# encoding:utf-8
__author__ = 'Zane'

import requests
from lxml import etree
from redis_queue import RedisQueue
from mongo_db import Zhihu_User_Data

#爬取的主要基类
class Zhihu_crawler():

    def __init__(self, url):
        self.queue = RedisQueue('zhihu', host='localhost', port=6379, db=0)
        self.url = url
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
                        , "Host":"www.zhihu.com"
                        , "Refer":"www.zhihu.com"
                        , "Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4"
                        , "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
                        , "Accept-Encoding":"gzip, deflate, sdch, br"
                        , "Cache-Control":"max-age=0"
                        , "Connection":"keep-alive"}

        #cookie
        self.cookies={"_zap":"aaf2a75d-0a1b-4863-b8a0-23ff0f4a9002"
                    , "_za":"e73a8db5-0824-4c36-b6a2-7a5378a046f7"
                    , "udid":'"AFAAY31blAmPTta9QIqu7S6lUdEK97RWDgg=|1457941793"'
                    , "d_c0":'"AGBAzqyTowmPTpYh7UrYZSjcr43LFX006Tw=|1461248461"'
                    , "_zap":"267bc327-098d-4d7c-85cb-3cfd13cd2e8e"
                    , "q_c1":"3b3a3dccecf1499ea32a0b2da9be35ec|1470149980000|1445741536000"
                    , "_xsrf":"8a812fd7745e54a8e8ab4ed815fa9001"
                    , "l_cap_id":'"YzQ3YzNhNzUxZjBlNDAzNTgwM2FhNzdlODI5NjAxZjY=|1472298711|d67a5a1c7e5fb41cfe2715e389c74ebc6132007d"'
                    , "cap_id":'"ZGQwYTE0MTM3ODk0NDUzOGFkM2RiNGYxYTNmYTc1YTM=|1472298711|8fd9f406e4786a9ca56227b61e7c6a2a5c0f4b42"'
                    , "login":'"ZDlmZjdkMTA4NTkwNDA0MDgyNTc0ZDczNWYyOWZiZTc=|1472298742|da8a20e1922c8dac52ec4a98bca68ffed83ce46c"'
                    , "n_c":'1'
                    , "s-t":"autocomplete"
                    , "s-q":"volley%2Cretrofit%2Cokhttp"
                    , "s-i":"1"
                    , "sid":"6vahoruo"
                    , "a_t":'"2.0AEAAukjbcgoXAAAATjPpVwBAALpI23IKAGBAzqyTowkXAAAAYQJVTfYL6VcAoZ3PJyuvTIR4Yl3RS9B_tCnMwHxnX7iDfjl2Ve7xk-Nk6RdV68h4_A=="'
                    , "z_c0":"Mi4wQUVBQXVramJjZ29BWUVET3JKT2pDUmNBQUFCaEFsVk45Z3ZwVndDaG5jOG5LNjlNaEhoaVhkRkwwSC0wS2N6QWZB|1472308814|21bb41cc3844239f4582374fc850ced4a5e8c564"
                    , "__utma":"51854390.226515891.1472287250.1472298703.1472307196.4"
                    , "__utmc":"51854390"
                    , "__utmz":"51854390.1472296126.2.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)"
                    , "__utmv":"51854390.100--|2=registration_date=20160827=1^3=entry_date=20151025=1"}

    def send_request(self):
        #关注者的url
        followees_url = self.url + '/followees'

        session = requests.session()
        session.proxies = {
            "http": "http://124.88.67.17.251:8685",
            "https": "http://223.67.136.218:8920",
        }

        #发起请求
        #避免Https的证书验证

        r = requests.get(followees_url, cookies = self.cookies, headers = self.headers, verify = True)

        try:
            r.raise_for_status()
        except requests.HTTPError as e:
            print e.message + ' HttpError'
        except requests.ConnectionError as e:
            print e.message

        content = r.text
        if r.status_code == requests.codes.ok:
            self.parse_users_content(content)
            print "requests success!"

    #判断是否数据存在
    def judge_data_have(self, name, datas):
        if datas:
            #print datas[0]
            return datas[0]
        else:
            #print name + " not exist!"
            return ''

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
        self.followees_urls=''

        tree = etree.HTML(html_source)

        self.user_name = self.judge_data_have("姓名", tree.xpath('//a[@class = "name"]/text()'))
        self.user_location = self.judge_data_have("位置", tree.xpath('//span[@class = "location item"]/@title'))
        self.user_gender = self.judge_data_have("性别", tree.xpath('//span[@class = "item gender"]/i/@class'))
        if self.user_gender:
            if 'female' in self.user_gender:
                self.user_gender = 'female'
            elif 'male' in self.user_gender:
                self.user_gender = 'male'

        followees = tree.xpath('//div[@class = "zu-main-sidebar"]//strong/text()')
        if followees:
            self.user_followees = tree.xpath('//div[@class = "zu-main-sidebar"]//strong/text()')[0]
            self.user_followers = tree.xpath('//div[@class = "zu-main-sidebar"]//strong/text()')[1]

        stats = tree.xpath('//div[@class = "zm-profile-header-info-list"]//strong/text()')
        if stats:
            self.user_be_agreed = tree.xpath('//div[@class = "zm-profile-header-info-list"]//strong/text()')[0]
            self.user_be_thanked = tree.xpath('//div[@class = "zm-profile-header-info-list"]//strong/text()')[1]

        self.user_education_school = self.judge_data_have("学校", tree.xpath('//span[@class = "education item"]/a/@title'))
        self.user_education_subject = self.judge_data_have("学科", tree.xpath('//span[@class = "education-extra item"]/a/@title'))
        self.user_employment = self.judge_data_have("公司", tree.xpath('//span[@class = "employment item"]/@title'))
        self.user_employment_extra = self.judge_data_have("公司", tree.xpath('//span[@class = "position item"]/@title'))
        self.user_intro = self.judge_data_have("简介", tree.xpath('//div[@class = "bio ellipsis"]/@title'))

        #添加到队列里面
        self.followees_urls = tree.xpath('//a[@class = "zg-link author-link"]/@href')
        for url in self.followees_urls:
            #url = url.replace("https", "http")
            self.queue.put(url)

        self.print_data_out()

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

        self.save_in_mongodb()

    #存储到mongodb数据库里面
    def save_in_mongodb(self):
        new_data = Zhihu_User_Data(
            user_name = self.user_name,
            user_gender = self.user_gender,
            user_location = self.user_location,
            user_followees = self.user_followees,
            user_followers = self.user_followers,
            user_be_agreed = self.user_be_agreed,
            user_be_thanked = self.user_be_thanked,
            user_education_school = self.user_education_school,
            user_education_subject = self.user_education_subject,
            user_employment = self.user_employment,
            user_employment_extra = self.user_employment_extra,
            user_intro = self.user_intro,
            followees_urls = self.followees_urls
        )
        new_data.save()


    #返回队列
    def get_queue(self):
        return self.queue



