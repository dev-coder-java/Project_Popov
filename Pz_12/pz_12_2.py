# В квадратной матрице элементы на главной диагонали увеличить в 2 раза
import random

n = int(input("Введите размер квадратной матрицы: "))

matrix = []
for i in range(n):
    while True:
        try:
            row = [random.randint(1, 100) for _ in range(n)]
            if len(row) != n:
                print(f"Ошибка: в строке должно быть {n} элементов!")
                continue
            matrix.append(row)
            break
        except ValueError:
            print("Ошибка! Вводите только целые числа через пробел.")

print("\nИсходная матрица:")
print(*map(str, matrix), sep='\n')

#for i in range(n):
 #   matrix[i][i] *= 2


matrix = [[val * 2 if i == j else val for j, val in enumerate(row)] for i, row in enumerate(matrix)]

print("\nМатрица после увеличения главной диагонали в 2 раза:")
print(*map(str, matrix), sep='\n')
