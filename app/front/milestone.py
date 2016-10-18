# -*- coding: utf-8 -*-
"""
__author__ = 'Zhipeng Du'
__mtime__ = '2016/10/18' '15:24'
"""
from . import front
from flask import render_template, request
from ..models import Milestone, Config, Category


@front.route('/milestone')
def milestone():
    old_title = Config.query.filter_by(key='title').first()
    old_subtitle = Config.query.filter_by(key='subtitle').first()
    web_title = old_title.value if old_title else ''
    web_subtitle = old_subtitle.value if old_subtitle else ''
    all_product_line_id = Category.query.filter_by(parents_id=3).all()
    this_product_line_id = request.args.get('product_line_id')
    this_product_id = request.args.get('product_id')
    all_product_id = []
    all_milestone = []
    if this_product_line_id:
        this_product_line = Category.query.get(int(this_product_line_id))
        all_product_id = this_product_line.tags
        if this_product_id:
            all_milestone = Milestone.query.filter_by(product_id=this_product_id).order_by(Milestone.publish_time.desc()).all()
    return render_template('front/milestone.html', web_title=web_title, web_subtitle=web_subtitle,
                           all_product_line_id=all_product_line_id,
                           this_product_line_id=int(this_product_line_id) if this_product_line_id else 0,
                           this_product_id=int(this_product_id) if this_product_id else 0,
                           all_product_id=all_product_id, all_milestone=all_milestone)
