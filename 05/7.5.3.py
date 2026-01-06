#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal:
    name = "动物"
    
dog = Animal()
cat = Animal()

print(dog.name)
print(cat.name)

Animal.name = "哺乳类动物"

print(dog.name)
print(cat.name)