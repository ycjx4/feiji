#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
文件功能: 多态（Polymorphism）示例 - 基于继承
说明: 本文件演示了面向对象编程中的多态特性，通过继承实现不同类的对象调用相同方法产生不同行为
用途: 学习多态的概念和在继承体系中的应用
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

def animal_say(animal: Animal):
    """
    多态函数：接收 Animal 类型的参数并调用其 say 方法
    
    参数:
        animal (Animal): Animal 类或其子类的实例
    
    功能: 
        演示多态性 - 同一个函数可以处理不同类型的对象，
        调用相同的方法名但执行不同的实现
    """
    animal.say()  # 根据传入对象的实际类型调用相应的 say 方法

# 创建 Dog 和 Cat 对象
dog = Dog()
cat = Cat()

# 多态调用：同一个函数，传入不同类型的对象，产生不同的行为
animal_say(dog)  # 输出 "Dog" - 调用 Dog 类的 say 方法
animal_say(cat)  # 输出 "Cat" - 调用 Cat 类的 say 方法
