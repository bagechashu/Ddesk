# -*- coding: utf-8 -*-
from . import front
from flask import render_template, request
from app import config
from flask_login import current_user
from ..models import  Demand, Config, User, Issue


@front.route('/query')
def query():
    web_title = Config.query.filter_by(key='title').first()
    all_question = Issue.query.order_by(Issue.create_time.desc()).all()
    all_demand = Demand.query.order_by(Demand.create_time.desc()).all()
    old_user = User.query.get(current_user.id)
    if current_user.is_authenticated:
        all_user_question = Issue.query.filter_by(creator_id=old_user.id).order_by(Issue.create_time.desc()).all()
        all_user_demand = Demand.query.filter_by(creator_id=old_user.id).order_by(Demand.create_time.desc()).all()
    else:
        all_user_question = None
        all_user_demand = None
    return render_template('query-list.html', all_question=all_question, all_demand=all_demand,
                           all_user_question=all_user_question, all_user_demand=all_user_demand, web_title=web_title)


@front.route('/query/details')
def query_details():
    web_title = Config.query.filter_by(key='title').first()
    cid = request.args.get('cid')
    pid = request.args.get('pid')
    create_time = None
    create_customer = None
    details = None
    feedback = None
    assignee = None
    title = None
    status = None
    p_done_time = None
    t_done_time = None
    if cid == '1':
        this_question = Issue.query.get_or_404(pid)
        create_time = this_question.create_time
        create_customer = this_question.creator.name
        details = this_question.details
        feedback = this_question.feedback
        if this_question.assignee:
            assignee = this_question.assignee.name
        else:
            assignee = '待分派'
        title = this_question.title
        status = config.ISSUE_STATUS[this_question.status]
    if cid == '2':
        this_demand = Demand.query.get_or_404(pid)
        create_time = this_demand.create_time
        create_customer = this_demand.creator.name
        details = this_demand.details
        feedback = this_demand.feedback
        if this_demand.assignee:
            assignee = this_demand.assignee.name
        else:
            assignee = '待分派'
        title = this_demand.title
        status = config.DEMAND_STATUS[this_demand.status]
        p_done_time = this_demand.p_done_time
        t_done_time = this_demand.t_done_time
    return render_template('query-details.html', create_time=create_time, create_customer=create_customer,
                           details=details, feedback=feedback, assignee=assignee, title=title, status=status, web_title=web_title, p_done_time=p_done_time, t_done_time=t_done_time)