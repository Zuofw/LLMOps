#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    :   2025/11/24 15:21
@Author  :   zfw
@Version :   1.0
@Desc    :   
"""

from dataclasses import dataclass

from flask import Flask, Blueprint
from injector import inject

from internal.handler import AppHandler


@inject
@dataclass
class Router:
    """路由"""
    app_handler: AppHandler

    def register_router(self, app: Flask):
        # 1.创建蓝图
        bp = Blueprint("app", __name__, url_prefix="")

        # 将url和handler绑定
        bp.add_url_rule("/ping", view_func=self.app_handler.ping)

        # 3.在应用上注册蓝图
        app.register_blueprint(bp);
