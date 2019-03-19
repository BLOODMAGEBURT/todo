# -*- coding: utf-8 -*-
from flask import request, jsonify

from app import db
from app.api import bp
from app.api.error import bad_request
from app.models import Item

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
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 15, type=int), 100)

    return jsonify(Item.to_collection_dict(Item.query, page=page, per_page=per_page, endpoint='api.get_items'))


@bp.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    return jsonify(Item.query.get_or_404(item_id).to_dict())


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
    data = request.get_json() or {}
    if not ('body' in data and 'status' in data and 'category_id' in data):
        return bad_request(400, 'body 、status 、category_id must be included')
    item = Item.query.get_or_404(item_id)
    item.from_dict(data)
    db.session.commit()
    return jsonify(item.to_dict())


@bp.route('/items/<item_id>')
def del_item(item_id):
    item = Item.query.get_or_404(item_id)
    item.status = 0
    db.session.commit()
    return jsonify(item.to_dict())
