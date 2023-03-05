# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

num = int(input())
power = 2

while num > power:
    print(power, end=" ")
    power *= 2