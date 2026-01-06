#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal:
    def say(self):
        print("Animal")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
dog.say()

cat = Cat()
cat.say()