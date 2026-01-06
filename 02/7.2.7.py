#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Dog:
    def __init__(self, name):
        self.__name = name
    
    def play(self):
        print("汪汪汪！ 我是", self.__name)


dog = Dog("旺财")
dog.play()

# 错误
print(dog.__name)
