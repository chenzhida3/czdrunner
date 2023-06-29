#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   redis.py
@Time    :   2023/06/29 15:44:05
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   redis相关操作
'''

from aioredis import Redis, DataError
from config import config

class MyRedis(Redis):
    """继承redis,并添加自己的方法"""
    pass

async def init_redis_pool() -> MyRedis:
    """连接redis"""
    redis = await MyRedis.from_url(url=config.REDIS_URI,
                                   encoding=config.GLOBAL_ENCODING,
                                   decode_responses=True,
                                   health_check_interval=30)
    return redis