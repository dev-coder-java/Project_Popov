# В матрице найти минимальный элемент в предпоследней строке
import random

n = int(input("Введите количество строк: "))

matrix = []
for i in range(n):
    while True:
        try:
            row = [random.randint(1, 100) for _ in range(3)]
            if not row:
                print("Строка не может быть пустой!")
                continue
            matrix.append(row)
            break
        except ValueError:
            print("Ошибка! Вводите только целые числа через пробел.")

print("\nИсходная матрица:")
for row in matrix:
    print(row)

if len(matrix) < 2:
    print("\nОшибка: матрица должна содержать минимум 2 строки.")
else:
    pe_row = matrix[-2]
    min_elem = min(pe_row)
    print(f"\nМинимальный элемент в предпоследней строке: {min_elem}")