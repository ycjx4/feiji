#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 演示类的实例方法定义和调用
class Dog:
    def __init__(self, name):
        self.name = name  # 实例属性
    
    # 实例方法：第一个参数必须是self，表示对象本身
    def play(self):
        print("汪汪汪！ 我是", self.name)  # 通过self访问实例属性


dog = Dog("旺财")
dog.play()  # 调用实例方法
