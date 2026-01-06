#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件功能: 类继承中的私有方法访问问题
说明: 本文件演示了 Python 中私有方法（以双下划线开头）无法在子类中直接访问的特性
用途: 学习 Python 中私有成员的访问限制和名称改编机制
"""

class Animal:
    """
    Animal 类：动物基类
    
    属性:
        __name (str): 私有属性，动物的名字（使用双下划线前缀表示私有）
    """
    
    def __init__(self, name):
        """
        初始化 Animal 对象
        
        参数:
            name (str): 动物的名字
        """
        self.__name = name  # 私有属性，外部和子类无法直接访问

    def __play(self):
        """
        私有方法：打印提示信息
        
        功能: 这是一个私有方法，子类无法直接调用
        """
        print("Animal, __play")  # 私有方法的输出

    def play(self):
        """
        公有方法：打印提示信息
        
        功能: 这是一个公有方法，子类可以正常调用
        """
        print("Animal, play")  # 公有方法的输出

class Dog(Animal):
    """
    Dog 类：狗类，继承自 Animal
    
    说明: 展示子类访问父类私有方法时的限制
    """
    
    def __init__(self):
        """
        初始化 Dog 对象
        
        功能: 调用父类的 __init__ 方法
        """
        super(Dog, self).__init__("旺财")  # 调用父类初始化方法

    def say(self):
        """
        Dog 类的 say 方法
        
        功能: 演示访问父类的公有方法和私有方法
        """
        self.play()  # 成功调用父类的公有方法

        # 错误：无法访问父类的私有方法 __play，因为它被名称改编为 _Animal__play
        self.__play()

# 创建 Dog 对象
dog = Dog()
# 调用 say 方法，会在尝试调用 self.__play() 时报错
dog.say()