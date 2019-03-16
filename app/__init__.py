# -*- coding: utf-8 -*-
from flask import Flask

from app.api import bp as api_bp
from config import Config
from flask_sqlalchemy import SQLAlchemy
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
app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

# register blueprint
app.register_blueprint(api_bp, url_prefix='/api')
