#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 演示Python的私有方法
class Dog:
    # 双下划线开头的方法是私有方法，只能在类内部调用
    def __say(self, name):
        print(name)

    # 公有方法：可以在类内部调用私有方法
    def play(self):
        self.__say("汪汪汪")  # 类内部可以调用私有方法


dog = Dog()
dog.play()  # 正确：通过公有方法间接调用私有方法

# 错误：私有方法无法从类外部直接调用
dog.__say()