#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    :   2025/11/24 16:08
@Author  :   zfw
@Version :   1.0
@Desc    :   
"""
from injector import Injector

from internal.router import Router
from internal.server import Http
from internal.handler import AppHandler

# 创建一个Binder来配置依赖注入
def configure(binder):
    binder.bind(AppHandler, AppHandler())

injector = Injector([configure])

app = Http(__name__, router=injector.get(Router))

if __name__ == "__main__":
    app.run(debug=True)