#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Dog:
    def __say(self, name):
        print(name)

    def play(self):
        self.__say("汪汪汪")


dog = Dog()
dog.play()

# 错误
dog.__say()