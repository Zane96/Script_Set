# -*- coding: utf-8 -*-
# encoding:utf-8
import redis
#使用redis模仿一个多消费者的队列
__Author__ = 'Zane'

class RedisQueue(object):

    def __init__(self, name, namespace='queue', setname='set', **redis_kwargs):
        #私有变量

        self.__db = redis.Redis(host='127.0.0.1', port=6379, db=0)
        self.key = '%s:%s' % (namespace, name)
        self.set = 'set'

    #返回队列长队
    def qsize(self):
        return self.__db.llen(self.key)

    #判断是否为空
    def empty(self):
        return self.qsize() == 0

    #添加一个元素, 这里我们添加url
    def put(self, url):
        if self.__db.sadd(self.set, url):
            self.__db.rpush(self.key, url)

    #获得元素,block:是否需要当没有元素的时候阻塞
    def get(self, block=True, timeout=None):
        if block:
            item = self.__db.blpop(self.key, timeout=timeout)
        else:
            item = self.__db.lpop(self.key)

        if item:
            item = item[1]

        return item