#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal:
    name = "动物"  # 类属性
    
dog = Animal()  # 创建实例对象
cat = Animal()

print(dog.name)  # 通过实例访问类属性
print(cat.name)

Animal.name = "哺乳类动物"  # 修改类属性

print(dog.name)  # 所有实例的类属性都被修改
print(cat.name)