#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )


def flowersSet():
    garden_set = set(garden)
    meadow_set = set(meadow)
    print(garden_set)
    print(meadow_set)
    print("Цветы, которые растут и там и там", garden_set & meadow_set)
    print("Цветы, которые растут в саду, но не растут на лугу", garden_set - meadow_set)
    print("Цветы, которые растут на лугу, но не ратут в саду", meadow_set - garden_set)
    return ""