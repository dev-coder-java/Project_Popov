# Дан список размера N и целые числа K и L (1 < K < L < N).
# Найти сумму элементов списка, кроме элементов с номерами от K до L включительно

import random
n = 10
N = [random.randint(1, 10) for _ in range(n)]

K = int(input("Введите целое число: "))
L = int(input("Введите целое число: "))

result = 0

for index, num in enumerate(N):
    if index < K or index > L:
        result += num

print(N)
print(result)