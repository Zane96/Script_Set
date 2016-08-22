# -*- coding: utf-8 -*-
# encoding:utf-8
__author__ = 'Zane'
import crawler, time
from multiprocessing import Pool

total = 20

def start_crawler(url, progress_name, num):
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

if __name__ == "__main__":
    zhihu_crawler = crawler.Zhihu_crawler("https://www.zhihu.com/people/xu-zhi-75-83")
    zhihu_crawler.send_request()
    zhihu_crawler.print_data_out()
    urls = zhihu_crawler.get_followees_url()
    i = 0
    p = Pool(2)
    for url in urls:
        i += 1
        time.sleep(1)
        p.apply_async(start_crawler, args=(url, i, 0,))

    p.close()
    p.join()

    print 'All progress end! total : ' + str(i)
