# -*- coding: utf-8 -*-
"""
__author__ = 'Zhipeng Du'
__mtime__ = '2016/10/18' '14:14'
"""
from . import back
from flask_login import login_required
from flask import render_template, redirect, url_for, flash, request
from ..models import db, Milestone, Category
from ..forms import MilestoneForm


@back.route('/milestone')
@login_required
def milestone():
    all_milestone = Milestone.query.order_by(Milestone.publish_time.desc()).all()
    return render_template('back/milestone.html', data=all_milestone)


@back.route('/milestone/add', methods=['GET', 'POST'])
@login_required
def add_milestone():
    form = MilestoneForm()
    form_pro_line_choice = []
    category_line = Category.query.filter_by(parents_id=3).all()
    for category in category_line:
        all_category_tag = category.tags
        tag_choice = (category.name, [(tag.id, tag.name) for tag in all_category_tag])
        form_pro_line_choice.append(tag_choice)
    form.product.choices = form_pro_line_choice
    if form.validate_on_submit():
        new_milestone = Milestone(product_id=form.product.data, title=form.title.data, details=form.details.data,
                                  publish_time=form.publish_time.data)
        db.session.add(new_milestone)
        db.session.commit()
        flash('新里程碑添加成功', 'is-success')
        return redirect(url_for('.milestone'))
    return render_template('back/milestoneAdd.html', form=form)


@back.route('/milestone/edit', methods=['GET', 'POST'])
@login_required
def edit_milestone():
    this_milestone = Milestone.query.get_or_404(request.args.get('id'))
    form = MilestoneForm(product=this_milestone.product_id, title=this_milestone.title, details=this_milestone.details,
                         publish_time=this_milestone.publish_time)
    form_pro_line_choice = []
    category_line = Category.query.filter_by(parents_id=3).all()
    for category in category_line:
        all_category_tag = category.tags
        tag_choice = (category.name, [(tag.id, tag.name) for tag in all_category_tag])
        form_pro_line_choice.append(tag_choice)
    form.product.choices = form_pro_line_choice
    if form.validate_on_submit():
        this_milestone.pro_line = form.product.data
        this_milestone.num = form.title.data
        this_milestone.details = form.details.data
        this_milestone.pub_time = form.publish_time.data
        db.session.add(this_milestone)
        db.session.commit()
        flash('版本信息已保存。', 'alert-success')
        return redirect(url_for('.milestone'))
    return render_template('back/milestoneEdit.html', form=form)