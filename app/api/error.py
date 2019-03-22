# -*- coding: utf-8 -*-
from flask import jsonify

from app import app, db

"""
-------------------------------------------------
   File Name：     error
   Description :
   Author :       burt
   date：          2019-03-17
-------------------------------------------------
   Change Activity:
                   2019-03-17:
-------------------------------------------------
"""


def bad_request(status_code, message):
    return jsonify(status_code, message)


@app.errorhandler(404)
def not_found_error(error):
    return bad_request(404, 'resource not found')


@app.errorhandler(500)
def not_found_error(error):
    db.session.rollback()
    return bad_request(500, 'server internal error')
