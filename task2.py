# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random


def fill_list(n):
    lst = []
    for i in range(n):
        lst.append(random.randint(-5, 5))
    return lst


def mult(lst):
    res = []
    if len(lst) % 2 == 0:
        for i in range(len(lst)//2):
            res.append(lst1[i] * lst1[len(lst1)-i-1])
    else:
        for i in range(len(lst)//2+1):
            res.append(lst1[i] * lst1[len(lst1)-i-1])
    return res


N = int(input('Количество элементов в списке: '))
lst1 = fill_list(N)
print(lst1)
# print(len(lst1))
res1 = mult(lst1)
print(res1)
