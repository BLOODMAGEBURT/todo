# -*- coding:utf-8 -*-
from flask_httpauth import HTTPTokenAuth
from app.models import User
from flask import g, request, jsonify
from app.api.error import bad_request
from app.api import bp
from app import db

"""
-------------------------------------------------
   File Name：     auth
   Description :
   Author :       burt
   date：        2019-03-23 23:22
-------------------------------------------------
   Change Activity:
                   2019-03-23 23:22
-------------------------------------------------
"""

token_auth = HTTPTokenAuth()


# 用户登录
@bp.route('/get_token', methods=['POST'])
def get_token():
    data = request.get_json() or {}
    if not ('username' in data and 'password_hash' in data):
        return bad_request(400, 'username, password_hash must be included')

    user = User.query.filter_by(username=data['username']).first()

    if user is None:
        return bad_request(400, 'username is not register')

    if not user.check_password(data['password_hash']):
        return bad_request(400, 'password is incorrect')

    token = user.get_token()
    db.session.commit()
    return jsonify(token=token)


# 验证
@token_auth.verify_token
def verify_token(token):
    g.current_user = User.check_token(token) if token else None
    return g.current_user is not None


# 处理错误
@token_auth.error_handler
def token_auth_error():
    return bad_request('401', 'token auth error')
