#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件功能: 类继承中的初始化问题示例
说明: 本文件演示了子类重写 __init__ 方法时，如果不调用父类的 __init__，会导致父类属性未初始化的问题
"""
class Animal:
    def __init__(self, name):
        self.name = name  # 设置动物的名字属性

    def play(self):
        print("我是", self.name)  # 输出动物的名字

class Dog(Animal):
    """
    Dog 类：狗类，继承自 Animal
    说明: 重写了 __init__ 方法，但没有调用父类的 __init__，导致 self.name 属性未初始化
    """
    
    def __init__(self):
        """
        初始化 Dog 对象
        注意: 这里只打印了"旺财"，但没有调用父类的 __init__ 方法，所以 self.name 属性未设置
        """
        print("旺财")  # 仅打印信息，未初始化父类属性
# 创建 Dog 对象
dog = Dog()
# 错误：调用 play 方法时会抛出 AttributeError 异常，因为 self.name 属性未定义
dog.play()