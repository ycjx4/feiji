#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件功能: Person 类的基础示例
说明: 本文件演示了如何创建一个简单的 Person 类，包含基本属性和方法
"""
class Person:

    def __init__(self, name, age, height, weight):
        """
        初始化 Person 对象
        
        参数:
            name (str): 姓名
            age (int): 年龄
            height (float): 身高（单位：米）
            weight (float): 体重（单位：公斤）
        """
        self.name = name      # 设置姓名属性
        self.age = age        # 设置年龄属性
        self.height = height  # 设置身高属性
        self.weight = weight  # 设置体重属性
    
    def print_person(self):
        """
        打印人员信息
        """
        print("姓名", self.name)    # 打印姓名
        print("年龄", self.age)     # 打印年龄
        print("身高", self.height)  # 打印身高
        print("体重", self.weight)  # 打印体重
# 创建 Person 对象实例，传入姓名、年龄、身高、体重
person = Person('零壹学堂', 1, 1.8, 70)
# 调用 print_person 方法打印人员信息
person.print_person()
#尝试git测试