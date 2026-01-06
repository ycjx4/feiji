#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 演示使用setter方法进行数据验证（封装的典型应用）
class Dog:
    def __init__(self, name):
        self.__name = name      # 私有属性：名字
        self.__age = None       # 私有属性：年龄，初始为None
        print(self.__name, "生成成功")

    # setter方法：用于安全地设置私有属性，可进行数据验证
    def set_age(self, age):
        if not isinstance(age, int):  # 类型检查
            print("输入的年龄必须是数字！")
            return False
        if age <= 0:                   # 值范围检查
            print("年龄必须大于0！")
            return False
        self.__age = age               # 验证通过后设置属性值

    def play(self):
        print("汪汪汪！我今年", self.__age)


dog = Dog("旺财")
dog.set_age("hello")  # 测试：传入字符串，验证失败
dog.set_age(-20)      # 测试：传入负数，验证失败
dog.set_age(3)        # 测试：传入有效值，验证成功
dog.play()
