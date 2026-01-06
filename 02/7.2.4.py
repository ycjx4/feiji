#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Dog类演示实例属性的定义和访问
class Dog:
    # __init__接收参数name，用于初始化实例属性
    def __init__(self, name):
        self.name = name  # self.name是实例属性，外部可访问
        self.age = 3      # 直接赋值的实例属性


# 创建Dog对象，传入名字参数
dog = Dog("旺财")

# 访问实例属性
print(dog.name)
print(dog.age)
