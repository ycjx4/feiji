#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件功能: 使用 super() 调用父类初始化方法
说明: 本文件演示了如何在子类的 __init__ 方法中正确调用父类的 __init__ 方法
用途: 学习使用 super() 函数解决继承中的初始化问题
"""
class Animal:

    def __init__(self, name):
        self.name = name  # 设置动物的名字属性

    def play(self):
        print("我是", self.name)  # 输出动物的名字

class Dog(Animal):
    def __init__(self):
        """
        初始化 Dog 对象
        功能: 使用 super() 调用父类的 __init__ 方法，传入"旺财"作为名字
        """
        # 调用父类的 __init__ 方法，初始化 name 属性为"旺财"
        super(Dog, self).__init__("旺财")

# 创建 Dog 对象
dog = Dog()
# 调用 play 方法，正常输出"我是 旺财"
dog.play()