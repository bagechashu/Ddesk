# -*- coding: utf-8 -*-
from config import load_config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from app.modules import dingtalk, alidayu
import os


app = Flask(__name__)
config = load_config()
app.config.from_object(config)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/uploads/')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.session_protection = 'strong'
login_manager.login_view = '.login'
login_manager.login_message = '请先登录再操作。'
login_manager.login_message_category = 'alert-danger is-danger'

# 接口初始化
# 钉钉
ding = dingtalk.DingTalk(config.DINGTALK_API_CID, config.DINGTALK_API_SECRET, config.DINGTALK_API_MSGID, config.DINGTALK_ROBOT_ACCESS_TOKEN)
# 阿里大鱼短信
alidayu = alidayu.RestApi(key=config.TAOBAO_API_KEY, secret=config.TAOBAO_API_SECRET, sms_free_sign_name='一融需求系统',
                          url='https://eco.taobao.com/router/rest')


# login回调函数
@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(int(user_id))


from .front import front
from .back import back
app.register_blueprint(front)
app.register_blueprint(back, url_prefix='/back')

