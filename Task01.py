# Задача:
# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

n = int(input('Введите количество элементов списка: '))

list = []
for i in range(n):
    list.append(random.randint(-n, n))
print(list)
list1 = [list[index] for index in range(0, len(list), 2)]
print(list1)
print(f'Сумма элементов стоящих на нечетной позиции = {sum(list1)}')