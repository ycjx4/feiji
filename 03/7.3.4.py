#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Animal:
    def __init__(self, name):
       self.__name = name  # 私有属性，外部和子类无法直接访问
    def __play(self):
        """
        私有方法：打印提示信息
        功能: 这是一个私有方法，子类无法直接调用
        """
        print("Animal, __play")  # 私有方法的输出
    def play(self):
        """
        公有方法：打印提示信息
        功能: 这是一个公有方法，子类可以正常调用
        """
        print("Animal, play")  # 公有方法的输出

class Dog(Animal):

    def __init__(self):
       super(Dog, self).__init__("旺财")  # 调用父类初始化方法

    def say(self):
        """
        Dog 类的 say 方法
        功能: 演示访问父类的公有方法和私有方法
        注意: 调用 self.__play() 会抛出 AttributeError 异常
        """
        self.play()  # 成功调用父类的公有方法

        # 错误：无法访问父类的私有方法 __play，会抛出 AttributeError 异常
        # 因为它被名称改编为 _Animal__play，而 self.__play 会被解析为 _Dog__play
        self.__play()

# 创建 Dog 对象
dog = Dog()
# 调用 say 方法，会在尝试调用 self.__play() 时抛出 AttributeError 异常
dog.say()