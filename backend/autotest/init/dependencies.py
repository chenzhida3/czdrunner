#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   dependencies.py
@Time    :   2023/06/30 15:50:58
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   设置全局request 便与上下文的访问
'''

from fastapi import Request
from autotest.corelibs.local import g

async def set_global_request(request: Request):
    g.request = request