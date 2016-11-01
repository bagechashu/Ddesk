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
from app import app, config
from . import front
from flask import render_template, request, send_from_directory, url_for
from ..models import Config
import json
import time
from werkzeug.utils import secure_filename
import os


@front.route('/commit/success')
def commit_success():
    old_title = Config.query.filter_by(key='title').first()
    old_subtitle = Config.query.filter_by(key='subtitle').first()
    web_title = old_title.value if old_title else ''
    web_subtitle = old_subtitle.value if old_subtitle else ''
    return render_template('front/success.html', web_title=web_title, web_subtitle=web_subtitle)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in config.ALLOWED_EXTENSIONS


# 文件下载接口
@front.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


# 文件接口
@front.route('/upload', methods=['POST'])
def upload():
    file = request.files['detail_img']
    path = app.config['UPLOAD_FOLDER']
    if file and allowed_file(file.filename):
        filename = str(time.time()) + secure_filename(file.filename)
        path = os.path.join(path, filename)
        file.save(path)
        print()
    return_info = {"success": "true", "file_path": url_for('.uploaded_file', filename=filename)}
    return json.dumps(return_info)


@front.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


@front.route('/favicon.ico')
def static_from_favicon():
    return send_from_directory(app.static_folder, request.path[1:])