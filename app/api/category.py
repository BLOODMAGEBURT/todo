# -*- coding: utf-8 -*-
from app.api import bp

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


@bp.route('/categorys', methods=['GET'])
def get_categorys():
    pass


@bp.route('/categorys/<cat_id>', methods=['GET'])
def get_category(cat_id):
    pass


@bp.route('/categorys', methods=['POST'])
def add_category():
    pass


@bp.route('/categorys/<cat_id>', methods=['PUT'])
def update_category(cat_id):
    pass


@bp.route('/categorys/<cat_id>', methods=['DELETE'])
def del_category(cat_id):
    pass
