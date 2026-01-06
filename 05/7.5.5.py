#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal:
    name = "动物"

    @classmethod
    def play(cls):
        print(cls.name, "playing")

Animal.play()
    
