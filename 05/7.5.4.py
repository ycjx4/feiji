#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal:
    name = "动物"  # 类属性

    @staticmethod  # 静态方法装饰器
    def play():
        print("playing")

Animal.play()  # 调用静态方法
    
