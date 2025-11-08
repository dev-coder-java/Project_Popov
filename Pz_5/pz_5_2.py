# Описать функцию Powerl(А, В) вещественного типа, находящую величину АВ по
# формуле АВ = exp(B*ln(A)) (параметры А и В - вещественные). В случае нулевого
# или отрицательного параметра А функция возвращает 0. С помощью этой функции
# найти степени А", В", С", если даны числа Р, А, В, С.
import math

try:
 A = int(input("Введите число: "))
 B = int(input("Введите число: "))
except ValueError:
    print("Введите число")


def Powerl(A, B):
    if A <= 0:
        return 0
    else:
        return math.exp(B * math.log(A))
result = Powerl(A, B)
print(result)

try:
 P = int(input("Введите число P: "))
 A = int(input("Введите число A: "))
 B = int(input("Введите число B: "))
 C = int(input("Введите число C: "))
except ValueError:
 print("Введите число")

A_P = Powerl(A, P)
B_P = Powerl(B, P)
C_P = Powerl(C, P)

print(f"A^{P} = {A_P}")
print(f"B^{P} = {B_P}")
print(f"C^{P} = {C_P}")