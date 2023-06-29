#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   mount.py
@Time    :   2023/06/29 17:23:21
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   挂载静态文件
'''
from fastapi import FastAPI
from config import config
from fastapi.staticfiles import StaticFiles


def init_mount(app: FastAPI):
    """挂载静态文件 -- https://fastapi.tiangolo.com/zh/tutorial/static-files/"""
    # 第一个参数为url路径参数, 第二参数为静态文件目录的路径, 第三个参数是FastAPI内部使用的名字
    app.mount(f"/{config.STATIC_DIR}", StaticFiles(directory=config.STATIC_DIR), name=config.STATIC_DIR)

