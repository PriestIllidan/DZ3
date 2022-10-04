# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random


def fill_list(n):
    lst = []
    for i in range(n):
        lst.append(random.randint(-5, 5))
    return lst


def sum_ood_elements(lst):
    res = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            res += lst[i]
            print(i)
    return res


N = int(input('Сколько чисел будет в массиве: '))
lst1 = fill_list(N)
print(lst1)
print(sum_ood_elements(lst1))
