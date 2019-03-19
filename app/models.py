# -*- coding: utf-8 -*-
import uuid
from datetime import datetime
from flask import url_for
from app import db

"""
-------------------------------------------------
   File Name：     models
   Description :
   Author :       burt
   date：          2019-03-16
-------------------------------------------------
   Change Activity:
                   2019-03-16:
-------------------------------------------------
"""


class PaginateMixIn(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **keywords):
        resource = query.paginate(page, per_page, False)
        data = {
            'items': [item.to_dict() for item in resource.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resource.pages,
                'total_items': resource.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page, **keywords),
                'next': url_for(endpoint, page=page+1, per_page=per_page, **keywords) if resource.has_next else None,
                'prev': url_for(endpoint, page=page-1, per_page=per_page, **keywords) if resource.has_prev else None
            }
        }
        return data


class Item(PaginateMixIn, db.Model):
    id = db.Column(db.String(36), primary_key=True)
    body = db.Column(db.String(300))
    post_on = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Integer, default=1)  # 1未完成 2已完成 0已删除
    category_id = db.Column(db.String(36), db.ForeignKey('category.id'))

    def to_dict(self):
        data = {
            'id': self.id,
            'body': self.body,
            'post_on': self.post_on.isoformat() + 'Z',
            'status': self.status,
            'category_id': self.category_id,
            'category_title': self.category.title
        }
        return data

    @staticmethod
    def get_id():
        return str(uuid.uuid4())

    def from_dict(self, data, new_item=False):
        for field in ['body', 'status', 'category_id']:
            if field in data:
                setattr(self, field, data[field])
        if new_item:
            self.id = self.get_id()


class Category(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    title = db.Column(db.String(50))
    items = db.relationship('Item', backref='category', lazy='dynamic')
