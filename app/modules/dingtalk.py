# -*- coding: utf-8 -*-
"""
__author__ = 'Zhipeng Du'
__mtime__ = '16/9/1' '14:35'
"""
import requests
import requests.packages.urllib3.util.ssl_
import json
from random import choice


requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
headers = {'content-type': "application/json"}
say = ['伟大的金主席教导我们：“该谁管的事情谁不管，该谁拿的工资谁别拿！” - 《金主席语录》',
       '伟大的金主席教导我们：“工单要是看不见，回头叫你请宝燕！” - 《金主席语录》',
       '伟大的金主席教导我们：“工单不处理，一会打死你！” - 《金主席语录》',
       '伟大的金主席教导我们：“谁的工单不反馈，回头一起吃最贵；括弧：你结账！” - 《金主席语录》',
       '伟大的金主席教导我们：“小小工单搞不好，同事关系完蛋鸟！” - 《金主席语录》',
       '伟大的金主席教导我们：“工单搞的快，处处惹人爱！” - 《金主席语录》',
       '伟大的金主席教导我们：“要想高总别找你，工单赶紧快处理！” - 《金主席语录》',
       '伟大的金主席教导我们：“同事们的需求是我们人生的追求，同事们的工单是我们心灵的港湾！” - 《金主席语录》',
       '伟大的金主席教导我们：“工单弄的好，美女少不了！” - 《金主席语录》',
       '伟大的金主席教导我们：“工单弄的快，人也长得帅！” - 《金主席语录》',
       '伟大的金主席教导我们：“今天工单搞不好，明天老婆跟人跑！” - 《金主席语录》',
       '伟大的金主席教导我们：“有人提问题，我们就要回复；有人提需求，我们就要处理；但有人胆敢要我们请客，我们就嫩（nèng)死他！” - 《金主席语录》',
       '伟大的金主席教导我们：“俗话说得好，工单快点搞！” - 《金主席语录》',
       '伟大的金主席教导我们：“是你的工单你不管，是你的工资给我拿！” - 《金主席语录》',
       '伟大的金主席教导我们：“雄关漫道真如铁，而今工单赶紧干！” - 《金主席语录》',
       '伟大的金主席教导我们：“多少工单，从来急，天地转，光阴迫，一万年太久，只争朝夕！” - 《金主席语录》']


class DingTalk:
    def __init__(self, key, secret, chatid):
        self.key = key
        self.secret = secret
        self.chatid = chatid

    def get_token(self):
        args = {'corpid': self.key, 'corpsecret': self.secret}
        r = requests.get('https://oapi.dingtalk.com/gettoken', params=args, verify=True)
        data = r.json()
        access_token = data['access_token']
        return access_token

    def msg(self, category, url, data):
        access_token = self.get_token()
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
            r_data = {'chatid': self.chatid, 'sender': 'dzp', 'msgtype': 'oa',
                      'oa': {'message_url': url, 'pc_message_url': url,
                             'head': {
                                 'bgcolor': 'FFED6C63',
                                 'text': '工单怎么没人管？是谁负责的？'},
                             'body': {
                                 'form': [{'key': '流水号:', 'value': data['num']}, {'key': '提出人:', 'value': data['create_customer']},
                                          {'key': '提出时间:', 'value': data['create_time']}, {'key': '诉求:', 'value': data['title']}],
                                 "content": choice(say)}}}

        if category == 5:
            r_data = {'chatid': self.chatid, 'sender': 'dzp', 'msgtype': 'oa',
                      'oa': {'message_url': url, 'pc_message_url': url,
                             'head': {
                                 'bgcolor': 'FF222324',
                                 'text': '这么久了还没搞完？'},
                             'body': {
                                 'form': [{'key': '流水号:', 'value': data['num']}, {'key': '提出人:', 'value': data['create_customer']},
                                          {'key': '提出时间:', 'value': data['create_time']}, {'key': '诉求:', 'value': data['title']}],
                                 "content": '久而不决是为何？及时反馈要记得！'}}}

        r = requests.post('https://oapi.dingtalk.com/chat/send?access_token=' + access_token, data=json.dumps(r_data),
                          verify=True, headers=headers)
        return r.json()

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
