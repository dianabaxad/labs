#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
#zoo.insert(1, "bear")
#print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль

def result():
    zoo.insert(1, "bear")
    print(zoo)
    zoo.extend(birds)
    print(zoo)
    zoo.remove('elephant')
    print(zoo)
    print("Лев и жаворонок сидят в клетках: ", zoo.index('lion') + 1, zoo.index('lark') + 1)