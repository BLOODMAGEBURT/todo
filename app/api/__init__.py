# -*- coding: utf-8 -*-
from flask import Blueprint

"""
-------------------------------------------------
   File Name：     __init__.py
   Description :
   Author :       Administrator
   date：          2019/3/16 0016
-------------------------------------------------
   Change Activity:
                   2019/3/16 0016:
-------------------------------------------------
"""
bp = Blueprint('api', __name__)

from app.api import item, error, category, user
