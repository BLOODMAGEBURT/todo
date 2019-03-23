# -*- coding: utf-8 -*-
from flask import request, jsonify

from app import db
from app.api import bp
from app.api.error import bad_request
from app.models import User, Category, get_id

"""
-------------------------------------------------
   File Name：     user
   Description :
   Author :       Administrator
   date：          2019/3/22 0022
-------------------------------------------------
   Change Activity:
                   2019/3/22 0022:
-------------------------------------------------
"""


@bp.route('/users', methods=['GET'])
def get_users():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 15, type=int), 100)
    data = User.to_collection_dict(User.query, page, per_page, 'api.get_users')
    return jsonify(data)


@bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())


# 新建用户
@bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json() or {}
    if not ('username' in data and 'password_hash' in data):
        return bad_request(400, 'username, password_hash must be included')
    if User.query.filter_by(username=data['username']).first():
        return bad_request(400, 'please use a different username')

    user = User()
    user.from_dict(data=data, new_user=True)
    db.session.add(user)

    # 同时创建默认的分类
    category = Category(id=get_id(), title='my default category', user=user)
    db.session.add(category)
    db.session.commit()
    return jsonify(user.to_dict())


@bp.route('/users', methods=['PUT'])
def update_user():
    pass


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
