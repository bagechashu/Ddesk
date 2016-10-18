# -*- coding: utf-8 -*-
"""
__author__ = 'Zhipeng Du'
__mtime__ = '2016/10/18' '18:35'
"""
from . import back
from ..forms import TagForm
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required
from ..models import db, Tag, Category


@back.route('/tag')
@login_required
def tag():
    all_tags = Tag.query.filter_by(status=True).order_by(Tag.id.desc()).all()
    return render_template('back/tag.html', all_tags=all_tags)


@back.route('/tag/add', methods=['GET', 'POST'])
@login_required
def add_tag():
    form = TagForm()
    all_category = Category.query.all()
    form.category_id.choices = [(category.id, category.name) for category in all_category]
    if form.validate_on_submit():
        new_tag = Tag(name=form.name.data, sequence=form.sequence.data, category_id=form.category_id.data)
        db.session.add(new_tag)
        db.session.commit()
        flash('添加Tag成功。', 'is-success')
        return redirect(url_for('.tag', status=1))
    return render_template('back/tagAdd.html', form=form)


@back.route('/tag/edit', methods=['GET', 'POST'])
@login_required
def edit_tag():
    old_tag = Tag.query.get_or_404(request.args.get('tag_id'))
    form = TagForm(name=old_tag.name, sequence=old_tag.sequence)
    all_category = Category.query.all()
    form.category_id.choices = [(category.id, category.name) for category in all_category]
    form.category_id.choices.remove((old_tag.category.id, old_tag.category.name))
    form.category_id.choices.insert(0, (old_tag.category.id, old_tag.category.name))
    if form.validate_on_submit():
        old_tag.name = form.name.data
        old_tag.sequence = form.sequence.data
        old_tag.category_id = form.category_id.data
        db.session.add(old_tag)
        db.session.commit()
        flash('Tag信息已更新', 'is-success')
        return redirect(url_for('.tag', status=1))
    return render_template('back/tagEdit.html', form=form)


@back.route('/tag/status')
@login_required
def status_tag():
    old_tag = Tag.query.get_or_404(request.args.get('tag_id'))
    if old_tag.status:
        old_tag.status = False
    else:
        old_tag.status = True
    db.session.add(old_tag)
    db.session.commit()
    flash('Tag状态已更新', 'is-success')
    return redirect(url_for('.tag', status=1))