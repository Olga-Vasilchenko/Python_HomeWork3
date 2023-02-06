# Задача:
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint

n = int(input('Введите количество элементов списка: '))

list = []
for i in range(n):
    list.append(randint(-n, n))
print(list)

def mult(list):
    mult = []
    for i in range ((len(list)+1)//2):
        mult.append(list[i]*list[len(list)-1-i])
    return mult
print(f'Произведение первого и последнего элемента списка = {mult(list)}')