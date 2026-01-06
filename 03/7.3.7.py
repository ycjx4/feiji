#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件功能: isinstance() 函数使用示例
说明: 本文件演示了如何使用 isinstance() 函数判断对象是否是某个类的实例
用途: 学习 Python 中的类型检查和继承关系判断
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
    
    说明: 重写了父类的 say 方法
    """
    
    def say(self):
        """
        重写父类的 say 方法
        
        功能: 打印 "Dog"
        """
        print("Dog")  # 输出狗的标识

class Cat(Animal):
    """
    Cat 类：猫类，继承自 Animal
    
    说明: 重写了父类的 say 方法
    """
    
    def say(self):
        """
        重写父类的 say 方法
        
        功能: 打印 "Cat"
        """
        print("Cat")  # 输出猫的标识

# 创建 Dog 和 Cat 对象
dog = Dog()
cat = Cat()

# 使用 isinstance() 检查对象类型
print(isinstance(dog, Dog))     # True: dog 是 Dog 类的实例
print(isinstance(dog, Animal))  # True: dog 也是 Animal 类的实例（因为继承关系）
print(isinstance(cat, Cat))     # True: cat 是 Cat 类的实例
print(isinstance(cat, Animal))  # True: cat 也是 Animal 类的实例（因为继承关系）