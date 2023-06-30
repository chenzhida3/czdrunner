#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   exceptions.py
@Time    :   2023/06/29 17:57:29
@Author  :   Chenzhida 
@Email   :   Chenzhida3@163.com
@Desc    :   重写异常方法
'''
import typing
from autotest.corelibs.codes import CodeEnum

class MyBaseException(Exception):
    def __init__(self, err_or_code: typing.Union[CodeEnum, str]):
        if isinstance(err_or_code, CodeEnum):
            # 用于检查一个对象是否是指定类或其子类的实例
            code = err_or_code.code
            msg = err_or_code.msg
        else:
            code = CodeEnum.PARTNER_CODE_FAIL.code
            msg = err_or_code
        self.code = code
        self.msg = msg
    # __str__(self) 方法用于给用户提供一个对象的简洁、易读的描述信息，
    # 通常用于将对象转换为字符串输出，可以通过 print() 等函数来调用。
    # 如果一个对象没有定义 __str__ 方法，则会使用__repr__ 方法代替，输出对象的“官方”字符串表示形式
    def __str__(self) -> str:
        return f"{self.code}:{self.msg}"
    
    def __repr__(self):
        return f"{self.code}:{self.msg}"
    
class IpError(MyBaseException):
    """ip错误"""
    def __init__(self):
        super(IpError, self).__init__("ip 错误")

class SetRedis(MyBaseException):
    """ Redis存储失败 """
    def __init__(self):
        super(SetRedis, self).__init__("Redis存储失败")

class IdNotExist(MyBaseException):
    """ 查询id不存在 """
    def __init__(self):
        super(IdNotExist, self).__init__("查询id不存在")

class UserNotExist(MyBaseException):
    """ 用户不存在 """
    def __init__(self):
        super(UserNotExist, self).__init__("用户不存在")

class AccessTokenFail(MyBaseException):
    """ 访问令牌失败 """
    def __init__(self):
        super(AccessTokenFail, self).__init__(CodeEnum.PARTNER_CODE_TOKEN_EXPIRED_FAIL)

class ErrorUser(MyBaseException):
    """ 错误的用户名或密码 """
    def __init__(self):
        super(ErrorUser, self).__init__("错误的用户名或密码")

class PermissionNotEnough(MyBaseException):
    """ 权限不足,拒绝访问 """
    def __init__(self):
        super(PermissionNotEnough, self).__init__("权限不足,拒绝访问")

class ParameterError(MyBaseException):
    """ 参数错误 """
    def __init__(self, err_code: typing.Union[CodeEnum, str]):
        super(ParameterError, self).__init__(err_code)

