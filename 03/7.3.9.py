#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Dog:
    def say(self):
        print("Dog")

class Cat:
    def say(self):
        print("Cat")

def animal_say(animal):
    animal.say()

dog = Dog()
cat = Cat()

animal_say(dog)
animal_say(cat)
