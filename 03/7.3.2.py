#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal:
    def __init__(self, name):
        self.name = name

    def play(self):
        print("我是", self.name)

class Dog(Animal):
    def __init__(self):
        print("旺财")

dog = Dog()

# 错误
dog.play()