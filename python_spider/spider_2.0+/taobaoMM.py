#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2016-08-10 22:30:05
# Project: taobaomm
#powerby PySpider
__author__ = 'Zane'

from pyspider.libs.base_handler import *
import os

PAGE_START = 1
PAGE_END = 30
DIR_PATH = '/Users/zane/programming/python-code/spider_2.0+/mm'

class Handler(BaseHandler):
    crawl_config = {
    }

    def __init__(self):
        self.base_url = 'https://mm.taobao.com/json/request_top_list.htm?page='
        self.page = PAGE_START
        self.total_page = PAGE_END
        self.tool = ImageTools()

    @every(minutes=24 * 60)
    def on_start(self):
        while self.page <= self.total_page:
            url = self.base_url + str(self.page)
            print url
            self.crawl(url, callback=self.index_page)
            self.page += 1

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc('.lady-name').items():
            self.crawl(each.attr.href, callback=self.detail_page, fetch_type='js')

    @config(priority=2)
    def detail_page(self, response):
        domain = 'https:' + response.doc('.mm-p-domain-info li > span').text()
        print domain
        if domain:
            self.crawl(domain, callback=self.domain_page)

    def domain_page(self, response):
        #获得mm名字
        name = response.doc('.mm-p-model-info-left-top dd > a').text()
        #获得文件存储路径
        dir_path = self.tool.mksirs(name)
        #获得全部内容信息
        brief = response.doc('.mm-aixiu-content').text()
        #保存信息
        self.tool.saveBrief(brief, dir_path)
        if dir_path:
            #获得全部图片内容
            imgs = response.doc('.mm-aixiu-content img').items()
            count = 1
            for img in imgs:
                extension = self.tool.getExtension(img.attr.src)
                filename = name + str(count) + '.' + extension
                count += 1
                #回调保存照片函数
                self.crawl(img.attr.src, callback=self.save_img,
                               save={'dir_path': dir_path, 'file_name': filename})

    def save_img(self, response):
        image = response.content
        dir_path = response.save['dir_path']
        filename = response.save['file_name']
        self.tool.saveImage(image, dir_path + '/' + filename)

class ImageTools:
    def __init__(self):
        self.path = DIR_PATH + '/'
        if not os.path.exists(self.path):
            os.makedirs(self.path)

    #生成每个mm的单独文件夹
    def mksirs(self, path):
        dir_path = self.path + path
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            return dir_path
        else:
            return dir_path

    #保存照片
    def saveImage(self, content, path):
        with open(path, 'wb') as f:
            f.write(content)

    #保存简介
    def saveBrief(self, content, path):
        brief_path = path + '简介'.decode('utf-8') + '.txt'
        with open(brief_path, 'wb') as f:
            f.write(content.encode('utf-8'))

    #获得图片的格式类型,通过url(jpg)
    def getExtension(self, url):
        extension = url.split('.')[-1]
        return extension