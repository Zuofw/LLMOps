#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    :   2025/11/24 11:51
@Author  :   zfw
@Version :   1.0
@Desc    :   
"""
from injector import inject, Injector


class A:
    name: str = "llmops"


@inject
class B:
    def __init__(self, a: A):
        self.a = a

    def print(self):
        print(self.a.name)


injector = Injector()

b_instance = injector.get(B)

b_instance.print()
