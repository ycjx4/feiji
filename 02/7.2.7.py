#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 演示Python的私有属性（名称改写机制）
class Dog:
    def __init__(self, name):
        self.__name = name  # 双下划线开头表示私有属性，外部无法直接访问
    
    def play(self):
        print("汪汪汪！ 我是", self.__name)  # 类内部可以访问私有属性


dog = Dog("旺财")
dog.play()  # 正确：通过方法间接访问私有属性

# 错误：私有属性无法从类外部直接访问
print(dog.__name)