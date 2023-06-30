#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   serialize.py
@Time    :   2023/06/30 11:44:53
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   序列化器
'''

from datetime import datetime
from fastapi.encoders import jsonable_encoder

from sqlalchemy import Row
from sqlalchemy.orm import DeclarativeMeta

def default_serialize(obj):
    """默认序序列化"""
    try:
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, Row):
            data = dict(zip(obj._fields, obj._data))
            return {key: default_serialize(value) for key, value in data.items()}
        if hasattr(obj, "__class__") and isinstance(obj.__class__, DeclarativeMeta):
            return {c.name: default_serialize(getattr(obj, c.name)) for c in obj.__table__.columns}
        return jsonable_encoder(obj)
    except TypeError as err:
        return repr(obj)
