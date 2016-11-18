# -*- coding: utf-8 -*-
# encoding:utf-8
__author__ = 'Zane'
import crawler
from multiprocessing import Pool
import multiprocessing
import time

def start_crawler (page):
    time.sleep(3)
    photo_crawler = crawler.photo_crawler(page)
    photo_crawler.send_request()

if __name__ == '__main__':

    pool = Pool(processes = 3)

    pages = []
    for i in range(1, 230):
        pages.insert(len(pages), i)

    pool.map(start_crawler, pages)