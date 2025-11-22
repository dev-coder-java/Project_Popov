#Дано множество А из N точек на плоскости и точка В (точки заданы своими
#координатами х, у). Найти точку из множества А, наиболее близкую к точке В.
#Расстояние R между точками с координатами (x1, y1) и (х2, У2) вычисляется по
#формуле: R=v(x2-x1)2+(y2-y1)2.

#Для хранения данных о каждом наборе точек следует использовать по два списка: первый
#список для хранения абсцисс, второй - для хранения ординат.

import math

N = int(input("Введите количество точек N: "))

xB = float(input("Введите координату x точки B: "))
yB = float(input("Введите координату y точки B: "))

x_coords = []
y_coords = []
for i in range(N):
    x = float(input(f"Введите координату x точки {i+1}: "))
    y = float(input(f"Введите координату y точки {i+1}: "))
    x_coords.append(x)
    y_coords.append(y)

min_dist = float('inf')
closest_point_index = -1

for i in range(N):
    x1 = x_coords[i]
    y1 = y_coords[i]
    dist = math.sqrt((x1 - xB) ** 2 + (y1 - yB) ** 2)
    if dist < min_dist:
        min_dist = dist
        closest_point_index = i

print(f"Наиболее близкая точка к точке B: ({x_coords[closest_point_index]}, {y_coords[closest_point_index]})")
