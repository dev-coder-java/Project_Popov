# Составить функцию, которая выполнит суммирования числового ряда

def my_sum(start, end):
    total = 0
    A = start
    while A <= end:
        total += A
        A += 1
    return total
try:
 start = int(input("Введите начало числового ряда: "))
 end = int(input("Введите конец числового ряда: "))
except ValueError:
    print("Введите число")


result = my_sum(start, end)

print(result)