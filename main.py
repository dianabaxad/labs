from distance import *
from circle import *
from movies import movies
from family import *
from operation import res
from zoo import  result
from songs import (totalTimeList, totalTimeDict)
from secret import secretMessage
from garden import flowersSet
from shop import printShops
from store import *
print("Задание 1")
print(distances)

print("\nЗадание 2")
print("Площадь круга: ", calculateArea(radius))
print("Точка№1: ", poinInCiecle(point_1, radius, center))
print("Точка№2: ", poinInCiecle(point_2, radius, center))

print("\nЗадание 3")
res()

print("\nЗадание 4")
movies()

print("\nЗадание 5")
print("Рост отца - ", getHightFather(), "см")
print("общий рост семьи - ", totalHight(), "см")

print("\nЗадание 6")
result()

print("\nЗадание 7")
print("Три песни звучат ", totalTimeList(), "минут")
print("А другие три песни", totalTimeDict(), "минут")

print("\nЗадание 8")
print(secretMessage())

print("\nЗадание 9")
flowersSet()

print("\nЗадание 10")
printShops()

print("\nЗадание 11")
lampCost()
tableCost()
sofaCost()
chairCost()