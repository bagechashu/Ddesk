# -*- coding: utf-8 -*-
class Config(object):
    DEBUG = False

    ISSUE_STATUS = {10: '待处理', 20: '处理中', 30: '处理完毕', 31: '处理完毕(有评价）', 40: '不予处理', 41: '搁置（现阶段无法处理）'}  # Status
