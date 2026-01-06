#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal:
    def __init__(self, name):
        self.name = name

    def play(self):
        print("我是", self.name)

class Dog(Animal):
    pass

dog = Dog("旺财")
dog.play()