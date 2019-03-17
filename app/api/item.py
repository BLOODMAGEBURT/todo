# -*- coding: utf-8 -*-
from app.api import bp
from flask import request, jsonify
from app.api.error import bad_request
from app.models import Item
from app import db
"""
-------------------------------------------------
   File Name：     item
   Description :
   Author :       burt
   date：          2019-03-16
-------------------------------------------------
   Change Activity:
                   2019-03-16:
-------------------------------------------------
"""


@bp.route('/items', methods=['GET'])
def get_items():
    return 'abs'


@bp.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    pass


@bp.route('/items', methods=['POST'])
def add_item():
    data = request.get_json() or {}
    if not ('body' in data and 'status' in data and 'category_id' in data):
        return bad_request(400, 'body, status, category_id must be included')
    item = Item()
    item.from_dict(data, new_item=True)
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict())


@bp.route('/items/<item_id>')
def update_item(item_id):
    pass


@bp.route('/items/<item_id>')
def del_item(item_id):
    pass
