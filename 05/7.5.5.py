#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal:
    name = "动物"  # 类属性

    @classmethod  # 类方法装饰器
    def play(cls):  # cls 参数指向类本身
        print(cls.name, "playing")

Animal.play()  # 调用类方法
    
