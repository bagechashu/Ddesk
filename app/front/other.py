# -*- coding: utf-8 -*-
"""
__author__ = 'duzhipeng'
__mtime__ = '16/8/11'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from app import app, config, up
from . import front
from flask import render_template, request, send_from_directory
from ..models import Config
import json
from datetime import datetime


@front.route('/commit/success')
def commit_success():
    old_title = Config.query.filter_by(key='title').first()
    old_subtitle = Config.query.filter_by(key='subtitle').first()
    web_title = old_title.value if old_title else ''
    web_subtitle = old_subtitle.value if old_subtitle else ''
    return render_template('front/success.html', web_title=web_title, web_subtitle=web_subtitle)


# 直接传图接口
@front.route('/upload/upyun', methods=['POST'])
def upyun():
    time = datetime.now()
    time_now = str(time.time())
    data = request.files['detail_img']
    key = '/easyrong/' + str(time.year) + '/' + str(time.month) + '/' + str(time.day) + '/' + time_now
    res = up.put(key, data)
    if res['file-type']:
        return_info = {"success": "true", "file_path": config.UPYUN_DOMAIN + key + "_600px"}
    return json.dumps(return_info)


@front.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


@front.route('/favicon.ico')
def static_from_favicon():
    return send_from_directory(app.static_folder, request.path[1:])