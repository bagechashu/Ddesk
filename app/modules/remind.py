# -*- coding: utf-8 -*-
"""
__author__ = 'Zhipeng Du'
"""
from app.models import db, Issue, Config
from app import ding
import datetime


def time_out_and_no_assignee():
    remind_task = Config.query.filter_by(key='remind_task').first()
    if remind_task is None:
        new_remind_task = Config(key='remind_task', value=datetime.datetime.now())
        db.session.add(new_remind_task)
        db.session.commit()
        remind_task = Config.query.filter_by(key='remind_task').first()
    if datetime.datetime.now() - datetime.datetime.strptime(remind_task.value.split(".")[0], "%Y-%m-%d %H:%M:%S") > datetime.timedelta(days=1):
        all_no_assignee_issue = Issue.query.filter_by(assignee_id=None).all()
        for item in all_no_assignee_issue:
            if datetime.datetime.now() - item.create_time > datetime.timedelta(days=1):
                extend = eval(item.extend)
                data = {'num': item.id, 'title': item.title, 'create_customer': item.creator.name,
                        'create_time': item.create_time.strftime("%Y-%m-%d %H:%M:%S"), 'class_id': extend['class_id']}
                if extend['class_id'] == 1:
                    url = 'http://chanpin.xinlonghang.cn/back/question/edit?id=' + str(item.id) + '&type=html5'
                    ding.msg(category=4, url=url, data=data)

                else:
                    url = 'http://chanpin.xinlonghang.cn/back/demand/edit?id=' + str(item.id) + '&type=html5' + '&class=' + str(extend['class_id'])
                    ding.msg(category=4, url=url, data=data)
        all_time_out_issue = Issue.query.filter(Issue.status < 30).all()
        for item in all_time_out_issue:
            if datetime.datetime.now() - item.create_time > datetime.timedelta(days=20):
                extend = eval(item.extend)
                data = {'num': item.id, 'title': item.title, 'create_customer': item.creator.name,
                        'create_time': item.create_time.strftime("%Y-%m-%d %H:%M:%S"), 'class_id': extend['class_id']}
                if extend['class_id'] == 1:
                    url = 'http://chanpin.xinlonghang.cn/back/question/edit?id=' + str(item.id) + '&type=html5'
                    ding.msg(category=5, url=url, data=data)

                else:
                    url = 'http://chanpin.xinlonghang.cn/back/demand/edit?id=' + str(item.id) + '&type=html5' + '&class=' + str(extend['class_id'])
                    ding.msg(category=5, url=url, data=data)
        remind_task.value = datetime.datetime.now()
        db.session.add(remind_task)
        db.session.commit()