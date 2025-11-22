def num(n):
    for number in range(3, n + 1, 2):
        print(number)

N = int(input("Введите N: "))

num1 = num(N)

print(f"Нечетные числа от 2 до {N}:")
