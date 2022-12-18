"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

Ввод: значение типа <float>
Вывод: значение типа <int>

Примеры:
6782.0
23

0.56
11
"""

def SumOfNumbers(numb):
    if numb < 0: 
        numb *= -1

    sumLeft = 0
    sumRight = 0

    numbLeft = numb
    while int(numbLeft) != 0:
        sumLeft += int(numbLeft % 10)
        numbLeft /= 10

    numbRight = numb
    while int((numbRight * 10) % 10) != 0:
        sumRight += int((numbRight * 10) % 10)
        numbRight *= 10

    return (sumLeft + sumRight)

userNumber = float(input('Enter any number: '))

print(f'Sum: {SumOfNumbers(userNumber)}') 