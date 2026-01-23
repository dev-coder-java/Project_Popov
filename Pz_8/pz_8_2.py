#Дана строка апельсины 45 991 63 100 12 яблоки 13 47 26 0 161,
# отражающая продажи продукции по дням в кг. Преобразовать информацию из строки в словари,
#с использованием функции найти максимальные продажи по каждому виду продукции, результаты вывести на экран.

def maximum(i):
    a = max(i)
    return a


sales = {}
produkt = None

text = "апельсины 45 991 63 100 12 яблоки 13 47 26 0 161"
b = text.split()
for x in b:
    if x.isdigit():
      sales[produkt].append(int(x))
    else:
        produkt = x
        sales[produkt] = []
print(sales)

for product, values in sales.items():
    print(product, ":", maximum(values))
