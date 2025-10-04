#Даны два числа. Вывести порядковый номер меньшего из них
try:
   a = int(input("Введите первое число: "))
   b = int(input("Введите второе число: "))
except ValueError:
     print("Ошибка")
     exit()
if a < b:
    print("первое число")
else:
    print("второе число")