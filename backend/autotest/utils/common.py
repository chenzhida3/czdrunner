#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   common.py
@Time    :   2023/06/29 15:20:31
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   工具通用方法
'''
import uuid

def get_str_uuid():
    return str(uuid.uuid4()).replace("-", "")