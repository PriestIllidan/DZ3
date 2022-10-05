# Задача 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def fill_list(n):
    lst = []
    for i in range(n):
        lst.append(float(input('Введите число для списка: ')))
    return lst


def find_rem(lst):
    res = []
    for i in range(len(lst)):
        res.append(lst[i] - int(lst[i]))
    return res


def find_diff_max_min(lst):
    e_max = lst[0]
    e_min = lst[0]
    for i in range(len(lst)):
        if lst[i] > e_max:
            e_max = lst[i]
        elif lst[i] < e_min:
            e_min = lst[i]
    print('Максимальное значение дробной части = ', e_max)
    print('Минимальное значение дробной части = ', e_min)
    return e_max - e_min


N = int(input('Введите длину списка: '))
lst1 = fill_list(N)
print(lst1)
res1 = find_rem(lst1)
print(res1)
elem_max = find_diff_max_min(res1)
print(elem_max)