#!/usr/bin/python3
# coding: utf-8
from flask import Blueprint, request
from flask import jsonify
from sqlalchemy.orm import Query

from mainapp.models import AppUser
import db

from common.crypo import encode4md5
from common.token_ import new_token

from common import sms_

user_blue = Blueprint('user_blue', __name__)


@user_blue.route('/login/', methods=('POST',))
def login():
    # 获取请求上传的json数据
    # {'name': '', 'pwd': ''}
    try:
        req_data = request.get_json()  # dict
        name, pwd = req_data['name'], req_data['pwd']
        if len(pwd.strip()) == 0:
            raise Exception('')
    except:
        return jsonify({
            'status': 1,
            'msg': '请求参数不完整，请提供name和pwd的json格式的参数'
        })

    query: Query = db.session.query(AppUser).filter(AppUser.name == name)
    if query.count() == 0:
        return jsonify({
            'status': 2,
            'msg': '查无此用户'
        })
    else:
        login_user: AppUser = query.first()
        if encode4md5(pwd) == login_user.auth_string:
            token = new_token()

            # 将token存在redis缓存中

            return jsonify({
                'status': 0,
                'msg': '登录成功',
                'token': token,
                'data': {
                    'name': login_user.name,
                    'email': login_user.email,
                    'photo': ''
                }
            })

        else:
            jsonify({
                'status': 3,
                'msg': '登录失败， 用户名或口令错误!',
            })


@user_blue.route('/send_code/', methods=('GET',))
def send_code():
    try:
        # 获取手机号
        phone = request.args.get('phone')
        sms_.send_code(phone)
    except:
        return jsonify({
            'status': 1,
            'msg': '发送失败，请重试'
        })

    return jsonify({
        'status': 0,
        'msg': '发送成功'
    })


@user_blue.route('/regist/', methods=('POST', ))
def regist():
    # {"phone": "", "code": ""}
    try:
        data = request.get_json()
        phone = data.get('phone')
        code = data.get('code')

        if sms_.validate_code(phone, code):
            user = AppUser()
            user.name = phone
            user.auth_string = encode4md5(phone[-6:])

            db.session.add(user)
            db.session.commit() # 提交事务

    except Exception as e:
        print(e)
        return jsonify({
            'status': 1,
            'msg': '注册失败'
        })

    return jsonify({
        'status': 0,
        'msg': '注册成功'
    })