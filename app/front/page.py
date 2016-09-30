# -*- coding: utf-8 -*-
from . import front
from flask import render_template, request
from ..models import Article, Config
from flask_login import current_user, login_required


@front.route('/page')
@login_required
def page():
    old_title = Config.query.filter_by(key='title').first()
    old_subtitle = Config.query.filter_by(key='subtitle').first()
    web_title = old_title.value if old_title else ''
    web_subtitle = old_subtitle.value if old_subtitle else ''
    this_page = Article.query.get_or_404(request.args.get('page_id'))
    return render_template('front/page.html', this_page=this_page, web_title=web_title, web_subtitle=web_subtitle)
