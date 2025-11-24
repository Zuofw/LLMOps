#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    :   2025/11/24 15:01
@Author  :   zfw
@Version :   1.0
@Desc    :
"""
from dataclasses import dataclass

from injector import inject


@inject
@dataclass
class AppHandler:
    """自定义控制器"""

    def ping(self):
        return {"ping": "pong"}
