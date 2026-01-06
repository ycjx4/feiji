#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件功能: 类的继承基础示例
说明: 本文件演示了 Python 中最简单的类继承方式
"""
class Animal:
    def __init__(self, name):
        """
        初始化 Animal 对象
        """
        self.name = name  # 设置动物的名字属性

    def play(self):
        print("我是", self.name)  # 输出动物的名字

class Dog(Animal):
    """
    Dog 类：狗类，继承自 Animal
    说明: 这是一个空的子类，没有重写任何方法，直接使用父类的所有方法
    """
    pass  # 空实现，继承父类的所有方法和属性
# 创建 Dog 对象，传入名字"旺财"
dog = Dog("旺财")
# 调用从父类继承的 play 方法
dog.play()