#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Dog:
    def __init__(self, name):
        self.name = name
        age = 3


dog = Dog("旺财")

print(dog.name)

# 错误
print(dog.age)
