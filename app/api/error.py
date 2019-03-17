# -*- coding: utf-8 -*-
from flask import jsonify

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
