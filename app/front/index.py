# -*- coding: utf-8 -*-
from . import front
from flask import render_template
from ..models import Config
from flask_login import login_required
from ..models import Article


@front.route('/')
@login_required
def index():
    old_title = Config.query.filter_by(key='title').first()
    old_subtitle = Config.query.filter_by(key='subtitle').first()
    web_title = old_title.value if old_title else ''
    web_subtitle = old_subtitle.value if old_subtitle else ''
    notice = Article.query.filter_by(title='首页公告').first()
    info = Article.query.filter_by(title='首页资料下载').first()
    video = Article.query.filter_by(title='首页视频下载').first()
    tips = Article.query.filter_by(title='首页小贴士').first()
    memo = Article.query.filter_by(title='首页备注').first()
    return render_template('front/index.html', web_title=web_title, web_subtitle=web_subtitle,
                           notice=notice.details, info=info.details, video=video.details, tips=tips.details, memo=memo.details)



