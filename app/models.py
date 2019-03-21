# -*- coding: utf-8 -*-
import uuid
from datetime import datetime
from flask import url_for
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

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
                'next': url_for(endpoint, page=page + 1, per_page=per_page, **keywords) if resource.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page, **keywords) if resource.has_prev else None
            }
        }
        return data


class Item(PaginateMixIn, db.Model):
    id = db.Column(db.String(36), primary_key=True)
    body = db.Column(db.String(300))
    post_on = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Integer, default=1)  # 1未完成 2已完成 0已删除
    category_id = db.Column(db.String(36), db.ForeignKey('category.id'))
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'))

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


class Category(PaginateMixIn, db.Model):
    id = db.Column(db.String(36), primary_key=True)
    title = db.Column(db.String(50))
    items = db.relationship('Item', backref='category', lazy='dynamic')
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'))

    def to_dict(self):
        data = {
            'id': self.id,
            'title': self.title,
            'items': [item.to_dict() for item in self.items]
        }

        return data

    @staticmethod
    def get_id():
        return str(uuid.uuid4())

    def from_dict(self, data: object, new_category: object = False) -> object:
        setattr(self, 'title', data['title'])
        if new_category:
            self.id = self.get_id()


class User(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)
    categorys = db.relationship('Category', backref='user', lazy='dynamic')
    items = db.relationship('Item', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
