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

def animal_say(animal: Animal):
    animal.say()

dog = Dog()
cat = Cat()

animal_say(dog)
animal_say(cat)
