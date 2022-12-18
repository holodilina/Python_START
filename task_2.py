"""
Напишите программу, которая принимает на вход натуральное число N и выдает список факториалов по основаниям от 1 до N

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
4
[1, 2, 6, 24]
"""

import math

userNumber = int(input('Enter any number: '))

for i in range(1, userNumber + 1):
    print(f'{i} - {math.factorial(i)}')

