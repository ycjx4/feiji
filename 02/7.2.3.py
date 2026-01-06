#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Dog:  # 定义一个类，面向对象的核心
    def __init__(self):  # 定义初始化方法，这是类实例化时自动调用的构造函数
        print("汪汪汪！")  # 初始化方法中的行为

dog = Dog()  # 创建类的实例，会自动调用构造方法