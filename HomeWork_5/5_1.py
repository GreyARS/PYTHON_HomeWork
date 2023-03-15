# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B 
# c помощью рекурсии.

def pow_n(a, b):
    if b == 0:
        return 1
    if b < 0:
        return pow_n(a, b + 1) * 1 / a
    return pow_n(a, b - 1) * a

print(pow_n(int(input("A: ")), int(input("B: "))))