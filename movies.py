#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from re import split

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!
comma1 = my_favorite_movies.index(',')
comma2 = my_favorite_movies.index(',', comma1 + 1)
comma3 = my_favorite_movies.index(',', comma2 + 1)
comma4 = my_favorite_movies.index(',', comma3 + 1)

def movies():
    first = my_favorite_movies[:comma1]
    last = my_favorite_movies[comma4+2:]
    second = my_favorite_movies[comma1+2:comma2]
    secondLast = my_favorite_movies[comma3+2:comma4]
    print("Первый фильм - ", first)
    print("Последний фильм - ", last)
    print("Второй фильм - ", second)
    print("Второй с конца фильм -" , secondLast)
    return ""