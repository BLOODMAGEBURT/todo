# -*- coding: utf-8 -*-
from app import db
from datetime import datetime
import uuid

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


class Item(db.Model):
    id = db.Column(db.String(36), primary_key=True)
    body = db.Column(db.String(300))
    post_on = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Integer, default=1)  # 1未完成 2已完成 0已删除
    category_id = db.Column(db.String(36), db.ForeignKey('category.id'))

    def to_dict(self):
        data = {
            'id': self.id,
            'body': self.body,
            'post_on': self.post_on,
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
