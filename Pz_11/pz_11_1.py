#Даны две последовательности. Найти элементы, различные для двух
#последовательностей и их среднее арифметическое.
l = [1, 2, 3, 4]
n = [3, 4, 5, 6]

elem = list(filter(lambda x: x not in n, l)) + list(filter(lambda x: x not in l, n))
print("Различные элементы:", elem)

m = sum(elem) / len(elem)
print("Среднее арифметическое:", m)
