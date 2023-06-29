#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   create_dir.py
@Time    :   2023/06/29 11:29:02
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   创建文件夹
'''
from pathlib import Path

def create_dir(file_name: str) -> Path:
    """创建文件夹"""
    path = Path(file_name).absolute().parent / file_name  # 拼接日志文件夹路径
    if not Path(path).exists():  # 如果文件夹不存在
        Path.mkdir(path)
    return path