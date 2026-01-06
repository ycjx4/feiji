#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Dog:
    def __say(self, name):  # 私有方法：只能类内部调用
        print(name)  # 打印名称
    
    def play(self):  # 实例方法通过私有方法打印内容
        self.__say("汪汪汪")  # 正确调用私有方法

dog = Dog()  # 创建对象
dog.play()  # 调用方法，间接调用私有方法

# 错误
dog.__say()  # 直接调用私有方法会报错