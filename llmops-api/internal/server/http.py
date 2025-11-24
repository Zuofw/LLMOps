#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    :   2025/11/24 16:04
@Author  :   zfw
@Version :   1.0
@Desc    :   
"""
from flask import Flask

from internal.router import Router


class Http(Flask):
    """http服务引擎"""

    # 非命名参数，命名参数
    def __init__(self, *args, router: Router, **kwargs):
        super().__init__(*args, **kwargs)
        # 注册路由
        router.register_router(self)
