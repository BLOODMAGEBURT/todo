# -*- coding: utf-8 -*-
from app.api import bp

"""
-------------------------------------------------
   File Name：     routes
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
    pass


@bp.route('/items/<item_id>')
def update_item(item_id):
    pass


@bp.route('/items/<item_id>')
def del_item(item_id):
    pass
