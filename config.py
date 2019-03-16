# -*- coding: utf-8 -*-
import os

"""
-------------------------------------------------
   File Name：     config
   Description :
   Author :       Administrator
   date：          2019/3/16 0016
-------------------------------------------------
   Change Activity:
                   2019/3/16 0016:
-------------------------------------------------
"""


class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-xu_bo_bo'

    basedir = os.path.abspath(os.path.dirname(__file__))
    # sql
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'todo.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # config admin email
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.qq.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or 1
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = [os.environ.get('ADMINS_MAIL')]

    # log file
    LOG_FILE = 'logs/todo.log'

    # paginate
    POSTS_PER_PAGE = 3

    # language for local
    LANGUAGES = ['en', 'es', 'zh_CN']

    # elastic search
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')

    # redis
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
