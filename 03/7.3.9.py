#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件功能: 鸭子类型（Duck Typing）示例 - 无继承的多态
说明: 本文件演示了 Python 中的鸭子类型特性，即使类之间没有继承关系，只要有相同的方法，就可以实现多态
用途: 学习 Python 中基于鸭子类型的多态实现
"""


class Dog:
    """
    Dog 类：狗类（独立类，没有父类）
    
    方法:
        say(): 输出 "Dog"
    """
    
    def say(self):
        """
        狗的叫声方法
        
        功能: 打印 "Dog"
        """
        print("Dog")  # 输出狗的标识

class Cat:
    """
    Cat 类：猫类（独立类，没有父类）
    
    方法:
        say(): 输出 "Cat"
    """
    
    def say(self):
        """
        猫的叫声方法
        
        功能: 打印 "Cat"
        """
        print("Cat")  # 输出猫的标识

def animal_say(animal):
    """
    鸭子类型函数：接收任何具有 say 方法的对象
    
    参数:
        animal: 任何具有 say() 方法的对象
    
    功能:
        演示鸭子类型 - "如果它走起来像鸭子，叫起来像鸭子，那它就是鸭子"
        不需要继承关系，只要对象有 say 方法就可以调用
    """
    animal.say()  # 调用传入对象的 say 方法

# 创建 Dog 和 Cat 对象
dog = Dog()
cat = Cat()

# 鸭子类型调用：虽然 Dog 和 Cat 没有继承关系，但都有 say 方法，所以都可以传入
animal_say(dog)  # 输出 "Dog"
animal_say(cat)  # 输出 "Cat"
