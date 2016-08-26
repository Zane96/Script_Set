# -*- coding: utf-8 -*-
# encoding:utf-8
__author__ = 'Zane'
import crawler
from multiprocessing import Pool
import gevent
from redis_queue import RedisQueue
import multiprocessing
import gevent.monkey
gevent.monkey.patch_socket()
gevent.monkey.patch_ssl()


'''
def start_crawler(url):
    n = num + 1
    #if n < 200:
    start_time = time.time()
    zhihu_crawler = crawler.Zhihu_crawler(url)
    zhihu_crawler.send_request()
    zhihu_crawler.print_data_out()
    end_time = time.time()
    print 'url is %s , num is %s, pro_name is %s, use time %s' % (url, n, progress_name, (end_time - start_time))
    urls = zhihu_crawler.get_followees_url()
    time.sleep(4)
    start_crawler(urls[0], progress_name, n)
    print 'end'
    #else:
        #print "#"*10 + str(progress_name) + ' is finfished total: ' + str(n)
'''

#获得一个新的用户信息
def creat_new_user(url):

    new_user = crawler.Zhihu_crawler(url)
    new_user.send_request()


#gevenlet的任务
def gevent_worker():
    while True:
        url = queue.get()
        if not url:
            break
        creat_new_user(url)

#gevenlet的启动者
def process_workder():
    works = []
    for i in range(20):
        works.append(gevent.spawn(gevent_worker()))
    gevent.joinall(works)

if __name__ == "__main__":
    pool = Pool(multiprocessing.cpu_count() * 2)
    zhihu_crawler = crawler.Zhihu_crawler("https://www.zhihu.com/people/xu-zhi-75-83")
    zhihu_crawler.send_request()
    queue = zhihu_crawler.get_queue()

    for i in range(20):
        url = queue.get()
        creat_new_user(url)

    pool.map_async(process_workder())
    pool.close()
    pool.join()


'''
    urls = zhihu_crawler.get_followees_url()
    i = 0
    p = Pool(2)
    for url in urls:
        i += 1
        time.sleep(1)
        p.apply_async(start_crawler, args=(url, i, 0,))
    #p.map_async(start_crawler, urls)
    p.close()
    p.join()
'''

