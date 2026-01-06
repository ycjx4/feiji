#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal:
    def say(self):
        print("Animal")

class Dog(Animal):
    def say(self):
        print("Dog")

class Cat(Animal):
    def say(self):
        print("Cat")

dog = Dog()
dog.say()

cat = Cat()
cat.say()