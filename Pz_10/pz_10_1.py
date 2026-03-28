#Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
#последовательности из целых положительных и отрицательных чисел. Сформировать
##новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Содержимое первого файла:
#Отрицательные элементы:
#Количество отрицательных элементов:
#Среднее арифметическое:

#Положительные элементы:
#Количество положительных элементов:
#Сумма положительных элементов:

l = '-5 3 -8 12 -1 7 -9 4 -2 6'
f1 = open('file1.txt', 'w')
f1.writelines(l)
f1.close()
f1 = open('file1.txt', 'r')
content = f1.read()
numb = content.split()
num1 = list(map(int, numb))
f1.close()

n = '10 -3 15 -7 8 20 -4 12 5 -1'
f2 = open('file2.txt', 'w')
f2.writelines(n)
f2.close()
f2 = open('file2.txt', 'r')
content = f2.read()
numb2 = content.split()
num2 = list(map(int, numb2))
f2.close()

neg_elem = [num for num in num1 if num < 0]
neg = len(neg_elem)
avg_negative = sum(neg_elem)

pos_elem = [num for num in num2 if num > 0]
positive = len(pos_elem)
sum_positive = sum(pos_elem)

f = open('result.txt', 'w', encoding='utf-8')
f.write('Содержимое первого файла:\n')
f.write(f'Отрицательные элементы: {neg_elem}\n')
f.write(f'Количество отрицательных элементов: {neg}\n')
f.write(f'Среднее арифметическое: {avg_negative:.2f}\n')
f.write('\n')
f.write('Содержимое второго файла:\n')
f.write(f'Положительные элементы: {pos_elem}\n')
f.write(f'Количество положительных элементов: {positive}\n')
f.write(f'Сумма положительных элементов: {sum_positive}\n')
f.close()

f = open('result.txt', 'r', encoding='utf-8')
print(f.read())
f.close()
