# -*- coding: utf-8 -*-
from .default import Config


class ProductionConfig(Config):
    # Flask
    DEBUG = True
    SECRET_KEY = ''

    # Mysql(SQLalchemy)
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # Other
    LOGIN_TOKEN = ''

    # DingTalk
    DINGTALK_ROBOT_ACCESS_TOKEN = ''

    # SMS API
    TAOBAO_API_KEY = ''
    TAOBAO_API_SECRET = ''
    DINGTALK_API_CID = ''
    DINGTALK_API_SECRET = ''
    DINGTALK_API_MSGID = ''