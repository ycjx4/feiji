#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件功能: 子类继承父类方法的基础示例
说明: 本文件演示了子类可以直接继承并使用父类的方法，无需重写
用途: 学习类继承的基本特性 - 方法复用
"""

class Animal:
    """
    Animal 类：动物基类
    
    方法:
        say(): 输出 "Animal"
    """
    
    def say(self):
        """
        动物叫声方法
        
        功能: 打印 "Animal"
        """
        print("Animal")  # 输出动物基类的标识

class Dog(Animal):
    """
    Dog 类：狗类，继承自 Animal
    
    说明: 空类，没有重写父类方法，直接继承父类的 say 方法
    """
    pass  # 空实现，使用父类的所有方法

class Cat(Animal):
    """
    Cat 类：猫类，继承自 Animal
    
    说明: 空类，没有重写父类方法，直接继承父类的 say 方法
    """
    pass  # 空实现，使用父类的所有方法

# 创建 Dog 对象
dog = Dog()
dog.say()  # 调用从父类继承的 say 方法，输出 "Animal"

# 创建 Cat 对象
cat = Cat()
cat.say()  # 调用从父类继承的 say 方法，输出 "Animal"