# -*- coding: utf-8 -*-
from app.api import bp
from flask import request, jsonify
from app.models import Category
from app.api.error import bad_request
from app import db
import logging

"""
-------------------------------------------------
   File Name：     category
   Description :
   Author :       Administrator
   date：          2019/3/19 0019
-------------------------------------------------
   Change Activity:
                   2019/3/19 0019:
-------------------------------------------------
"""
logging.basicConfig(level=logging.INFO)


@bp.route('/categorys', methods=['GET'])
def get_categorys():
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 15, type=int), 100)
    resource = Category.to_collection_dict(Category.query, page, per_page, 'api.get_categorys')
    return jsonify(resource)


@bp.route('/categorys/<cat_id>', methods=['GET'])
def get_category(cat_id):
    data = Category.query.get_or_404(cat_id)
    return jsonify(data.to_dict())


@bp.route('/categorys', methods=['POST'])
def add_category():
    data = request.get_json() or {}
    if 'title' not in data:
        bad_request(400, 'title must be included')

    if Category.query.filter_by(title=data['title']).first() is not None:
        bad_request(400, 'please use a different title')

    category = Category()
    category.from_dict(data, new_category=True)
    db.session.add(category)
    db.session.commit()
    return jsonify(category.to_dict())


@bp.route('/categorys/<cat_id>', methods=['PUT'])
def update_category(cat_id):
    category = Category.query.get(cat_id)
    if category is None:
        return bad_request(400, 'category not find')

    data = request.get_json() or {}
    if 'title' not in data:
        return bad_request(400, 'title must be included')
    old_category = Category.query.filter_by(title=data['title']).first()

    if old_category is not None and old_category.id != cat_id:
        # logging.info('category.id:{} , cat_id: {}'.format(old_category.id, cat_id))
        return bad_request(400, 'please use a different title')
    category.from_dict(data)
    db.session.commit()
    return jsonify(category.to_dict())


@bp.route('/categorys/<cat_id>', methods=['DELETE'])
def del_category(cat_id):
    pass
