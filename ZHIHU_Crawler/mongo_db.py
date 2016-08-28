# -*- coding: utf-8 -*-
# encoding:utf-8
__author__ = 'Zane'

#mongodb的user 文档

import mongoengine
from mongoengine import *
import datetime

#collect
mongoengine.connect('zhihu_user_data', host='mongodb://0.0.0.0:27017')

class Zhihu_User_Data(mongoengine.Document):

    user_name = mongoengine.StringField(max_length=200, required=True)
    user_gender = mongoengine.StringField(max_length=200, required=True)
    user_location = mongoengine.StringField(max_length=200, required=True)
    user_followees = mongoengine.StringField(max_length=200, required=True)
    user_followers = mongoengine.StringField(max_length=200, required=True)
    user_be_agreed = mongoengine.StringField(max_length=200, required=True)
    user_be_thanked = mongoengine.StringField(max_length=200, required=True)
    user_education_school = mongoengine.StringField(max_length=200, required=True)
    user_education_subject = mongoengine.StringField(max_length=200, required=True)
    user_employment = mongoengine.StringField(max_length=200, required=True)
    user_employment_extra = mongoengine.StringField(max_length=200, required=True)
    user_intro = mongoengine.StringField(max_length=200, required=True)
    followees_urls = mongoengine.ListField()

    date_modified = DateTimeField(default=datetime.datetime.now)