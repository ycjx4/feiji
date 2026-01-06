#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def print_person(self):
        print("姓名", self.name)
        print("年龄", self.age)
        print("身高", self.height)
        print("体重", self.weight)


person = Person('零壹学堂', 1, 1.8, 70)
person.print_person()
