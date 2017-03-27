# -*- coding: utf-8 -*-
"""
__author__ = 'Zhipeng Du'
__mtime__ = '16/9/1' '14:35'
"""
import requests
import requests.packages.urllib3.util.ssl_
import json


requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
headers = {'content-type': "application/json"}


class DingTalk:
    def __init__(self, key, secret, chatid, token):
        self.key = key
        self.secret = secret
        self.chatid = chatid
        self.token = token

    def get_token(self):
        args = {'corpid': self.key, 'corpsecret': self.secret}
        r = requests.get('https://oapi.dingtalk.com/gettoken', params=args, verify=True)
        data = r.json()
        access_token = data['access_token']
        return access_token

    def msg(self, category, url, data):
        access_token = self.get_token()
        robot_access_token = self.token
        r_data = {}
        if category == 1:
            r_data = {'chatid': self.chatid, 'sender': 'dzp', 'msgtype': 'oa',
                      'oa': {'message_url': url, 'pc_message_url': url,
                             'head': {'bgcolor': 'FF97CD76', 'text': '有问题来啦!'},
                             'body': {
                                 'form': [{'key': '流水号:', 'value': data['num']},
                                          {'key': '提出人:', 'value': data['create_customer']},
                                          {"key": "产品线:", "value": data['category']}],
                                 "content": "点击「查看详情」登录需求管理系统后，即可在钉钉里处理问题"}}}
        if category == 2:
            r_data = {'chatid': self.chatid, 'sender': 'dzp', 'msgtype': 'oa',
                      'oa': {'message_url': url, 'pc_message_url': url,
                             'head': {'bgcolor': 'FF1FC8DB', 'text': '有设计需求来啦!'},
                             'body': {
                                 'form': [{'key': '流水号:', 'value': data['num']}, {'key': '提出人:', 'value': data['create_customer']},
                                          {'key': '需求类型:', 'value': data['type']}, {'key': '支持内容:', 'value': data['support']},
                                          {"key": "设计类型:", "value": data['des_type']}],
                                 "content": "点击「查看详情」登录需求管理系统后，即可在钉钉里处理需求"}}}
        if category == 3:
            r_data = {'chatid': self.chatid, 'sender': 'dzp', 'msgtype': 'oa',
                      'oa': {'message_url': url, 'pc_message_url': url,
                             'head': {
                                 'bgcolor': 'FFA263ED',
                                 'text': '有产品需求来啦!'},
                             'body': {
                                 'form': [{'key': '流水号:', 'value': data['num']}, {'key': '提出人:', 'value': data['create_customer']},
                                          {'key': '需求类型:', 'value': data['type']}, {'key': '需求受众:', 'value': data['audience']},
                                          {"key": "需求来源:", "value": data['source']}, {"key": "产品线:", "value": data['category']}],
                                 "content": "点击「查看详情」登录需求管理系统后，即可在钉钉里处理需求"}}}
        if category == 4:
            content = str(data['create_customer']) + ' 在 ' + str(data['create_time']) + ' 提出的「' + str(data['title']) \
                      + '」，超过了受理时限尚无人受理，请群内同事尽快受理。' + str(url)
            r_data = {'msgtype': 'text',
                      'text': {'content': content}, 'at': {'atMobiles': [], 'isAtAll': 1}}

        if category == 5:
            content = str(data['create_customer']) + ' 在 ' + str(data['create_time']) + '提出的「' + str(data['title']) \
                      + '」，超过了规定的处理时间且没有任何反馈，请被@到的人及时登录后台处理。' + str(url)
            r_data = {'msgtype': 'text',
                      'text': {'content': content}, 'at': {'atMobiles': [data['assignee']], 'isAtAll': 0}}

        if category < 4:
            r = requests.post('https://oapi.dingtalk.com/chat/send?access_token=' + access_token, data=json.dumps(r_data),
                          verify=True, headers=headers)
        else:
            r = requests.post('https://oapi.dingtalk.com/robot/send?access_token=' + robot_access_token, data=json.dumps(r_data),
                              verify=True, headers=headers)

        return True

    def get_department(self):
        access_token = {'access_token': self.get_token()}
        r = requests.get('https://oapi.dingtalk.com/department/list', params=access_token)
        js_data = r.json()
        data = js_data['department']
        return data

    def get_user(self, department_id):
        args = {'access_token': self.get_token(), 'department_id': department_id}
        r = requests.get('https://oapi.dingtalk.com/user/list', params=args)
        js_data = r.json()
        data = js_data['userlist']
        return data
