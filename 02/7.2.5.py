#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 演示局部变量与实例属性的区别
class Dog:
    def __init__(self, name):
        self.name = name  # self.name是实例属性，可在类外访问
        age = 3           # age是局部变量，只在__init__方法内有效


dog = Dog("旺财")

print(dog.name)  # 正确：访问实例属性

# 错误：age是局部变量，不是实例属性，无法通过dog.age访问
print(dog.age)
