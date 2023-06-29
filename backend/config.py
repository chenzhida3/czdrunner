#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   config.py
@Time    :   2023/06/28 18:43:55
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   后台配置文件
'''
from dataclasses import Field
import typing
from pydantic import BaseSettings

project_desc = "🎉czdrunner项目 接口汇总🎉"
__version__ = "2.1.0"

class Configs(BaseSettings):
    PROJECT_DESC: str = project_desc  # 项目描述
    PROJECT_VERSION: typing.Union[int, str] = __version__

    GLOBAL_ENCODING: str = 'utf8'  # 全局编码

    # 日志部分
    LOGGER_DIR: str = "logs"  # 日志文件夹名
    LOGGER_NAME: str = 'czdrunner.log'  # 日志文件名  (时间格式 {time:YYYY-MM-DD_HH-mm-ss}.log)
    LOGGER_LEVEL: str = 'INFO'  # 日志等级: ['DEBUG' | 'INFO']
    LOGGER_ROTATION: str = "10 MB"  # 日志分片: 按 时间段/文件大小 切分日志. 例如 ["500 MB" | "12:00" | "1 week"]
    LOGGER_RETENTION: str = "7 days"  # 日志保留的时间: 超出将删除最早的日志. 例如 ["1 days"]

    # redis
    REDIS_URI: str = Field(..., env="REDIS_URI")  # redis

    class Config:
        case_sensitive = True  # 区分大小写
        env_file = ".env"

config = Configs()