#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Dog:  # \/- 定义一个类
    def __init__(self, name):  # 初始化方法，包含名称参数
        self.name = name  # 设置实例的名称属性
    
    def play(self):  # 定义实例方法
        print("汪汪汪！ 我是", self.name)  # 打印对象的名称属性

dog = Dog("旺财")  # 创建对象，并初始化实例属性
dog.play()  # 调用类的实例方法