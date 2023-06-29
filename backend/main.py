#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   main.py
@Time    :   2023/06/28 18:39:02
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   后台程序总入口
'''
import uvicorn
from fastapi import FastAPI

from autotest.config import config
from autotest.corelibs.logger import init_logger, logger
from autotest.db.redis import init_redis_pool
from autotest.init.mount import init_mount

app = FastAPI(title="czdrunnrt",
              description=config.PROJECT_DESC,
              version=config.PROJECT_VERSION)

async def init_app():
    """应用注册中心"""
    init_mount(app)  # 挂载静态文件
    init_logger()
    logger.info("日志初始化成功！！！")  # 初始化日志

@app.on_event("startup")
async def startup():
    await init_app()  # 加载
    app.state.redis = await init_redis_pool()
    logger.info("初始化redis连接池")

@app.on_event("shutdown")
async def shutdown():
    await app.state.redis.close()  # 关闭redis
    logger.info("关闭redis连接池")


if __name__ == '__main__':
    uvicorn.run(app='main:app', host="127.0.0.1", port=8001, reload=True)
