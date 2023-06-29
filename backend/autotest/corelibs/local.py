#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   local.py
@Time    :   2023/06/29 15:08:17
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   重写本地魔术方法
'''
from contextvars import ContextVar
import typing

class Local:
    __slots__ = ("_storage",)

    def __init__(self) -> None:
        object.__setattr__(self, "_storage", ContextVar("local_storage"))
    
    def __iter__(self) -> typing.Iterator[typing.Tuple[int, typing.Any]]:
        return iter(self._storage.get({}).items())
    
    def __release_local__(self) -> None:
        # 释放当前线程的本地变量, 避免内存泄漏
        self._storage.set({})

    def __getattr__(self, name: str) -> typing.Any:
        # 用于在访问一个不存在的属性时触发
        values = self._storage.get({})
        try:
            return values[name]
        except KeyError:
            return None
    
    def __setattr__(self, name: str, value: typing.Any) -> None:
        # 用于在设置一个属性时触发
        values = self._storage.get({}).copy()
        values[name] = value
        self._storage.set(values)
    
    def __delattr__(self, name: str) -> None:
        # 用于在删除一个属性时触发
        values = self._storage.get({}).copy()
        try:
            del values[name]
            self._storage.set(values)
        except KeyError:
            ...

g = Local()