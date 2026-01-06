#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Dog:
    def __init__(self, name):
        self.__name = name
        self.__age = None
        print(self.__name, "生成成功")

    def set_age(self, age):
        if not isinstance(age, int):
            print("输入的年龄必须是数字！")
            return False
        if age <= 0:
            print("年龄必须大于0！")
            return False
        self.__age = age

    def play(self):
        print("汪汪汪！我今年", self.__age)


dog = Dog("旺财")
dog.set_age("hello")
dog.set_age(-20)
dog.set_age(3)
dog.play()
