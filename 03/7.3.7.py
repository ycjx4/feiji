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
cat = Cat()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(cat, Cat))
print(isinstance(cat, Animal))