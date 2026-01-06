#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件功能: 方法重写（Method Overriding）示例
说明: 本文件演示了子类如何重写父类的方法，实现不同的行为
用途: 学习面向对象编程中的方法重写特性
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
    
    说明: 重写了父类的 say 方法，输出 "Dog"
    """
    
    def say(self):
        """
        重写父类的 say 方法
        
        功能: 打印 "Dog"，替代父类的实现
        """
        print("Dog")  # 输出狗的标识，覆盖父类方法

class Cat(Animal):
    """
    Cat 类：猫类，继承自 Animal
    
    说明: 重写了父类的 say 方法，输出 "Cat"
    """
    
    def say(self):
        """
        重写父类的 say 方法
        
        功能: 打印 "Cat"，替代父类的实现
        """
        print("Cat")  # 输出猫的标识，覆盖父类方法

# 创建 Dog 对象
dog = Dog()
dog.say()  # 调用重写后的 say 方法，输出 "Dog"

# 创建 Cat 对象
cat = Cat()
cat.say()  # 调用重写后的 say 方法，输出 "Cat"