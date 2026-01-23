# Дан список размера N и целые числа K и L (1 < K < L < N).
# Найти сумму элементов списка, кроме элементов с номерами от K до L включительно
import random

n = int(input("Введите размер списка N: "))
N = [random.randint(1, 10) for _ in range(n)]

K = int(input())
L = int(input())

result = 0
for index in range(n):
    if index < K or index > L:
        result += N[index]

print("Список:", N)
print("Сумма элементов, кроме элементов с индексами от K до L включительно:", result)