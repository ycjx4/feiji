#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal:
    def __init__(self, name):
        self.__name = name

    def __play(self):
        print("Animal, __play")

    def play(self):
        print("Animal, play")

class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__("旺财")

    def say(self):
        self.play()

        # 错误
        self.__play()

dog = Dog()
dog.say()