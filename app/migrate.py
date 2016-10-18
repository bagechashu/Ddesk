# -*- coding: utf-8 -*-
"""
__author__ = 'Zhipeng Du'
__mtime__ = '16/9/5' '17:42'
"""
from .models import db, Version, Milestone


def upgrade():
    old_data = Version.query.all()
    for item in old_data:
        new_m = Milestone(title=item.num, details=item.details, product_id=item.pro_line, publish_time=item.pub_time)
        db.session.add(new_m)
        db.session.commit()
    print('all tasks is done!')


if __name__ == '__main__':
    upgrade()