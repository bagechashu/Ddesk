# -*- coding: utf-8 -*-
"""
__author__ = 'Zhipeng Du'
__mtime__ = '2016/9/30' '18:08'
"""
from . import back
from flask_login import login_required, current_user
from flask import render_template, redirect, url_for, flash, request
from app import ding
from flask_login import login_user, logout_user
from ..models import Issue
import datetime


@back.route('/remind')
@login_required
def remind():
    this_issue = Issue.query.get(request.args.get('id'))
    extend = eval(this_issue.extend)
    data = {'num': this_issue.id,  'title': this_issue.title, 'create_customer': this_issue.creator.name,
            'create_time': this_issue.create_time.strftime("%Y-%m-%d %H:%M:%S"), 'class_id': extend['class_id']}
    if current_user.super_admin:
        if request.args.get('c') == 'q':
            url = 'http://chanpin.xinlonghang.cn/back/question/edit?id=' + str(this_issue.id) + '&type=html5'
            ding.msg(category=4, url=url, data=data)
            flash('已发出夺命叩。', 'is-success')
            return redirect(url_for('.question'))
        else:
            url = 'http://chanpin.xinlonghang.cn/back/demand/edit?id=' + str(this_issue.id) + '&type=html5' + '&class=' + str(extend['class_id'])
            ding.msg(category=4, url=url, data=data)
            flash('已发出夺命叩。', 'is-success')
            return redirect(url_for('.demand'))
    else:
        flash('请勿越权操作。', 'is-danger')
        logout_user()
        return redirect(url_for('.login'))