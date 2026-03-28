#Из предложенного текстового файла (text18-21.txt) вывести на экран его содержимое,
#количество знаков препинания. Сформировать новый файл, в который поместить текст в
#стихотворной форме выведя строки в обратном порядке.


print("Содержимое файла")
f = open('text18-21.txt', 'r', encoding='utf-8')
print(f.read())
f.close()
f = open('text18-21.txt', 'r', encoding='utf-8')
content = f.read()
f.close()

punct = '.,!?;:—–-"\'()[]{}«»'
count = 0
for char in content:
    if char in punct:
        count += 1

print(f"\nКоличество знаков препинания:")
print(count)

lines = content.splitlines()
reversed_lines = lines[::-1]
reversed_text = '\n'.join(reversed_lines)

f = open('text18-21_reversed.txt', 'w', encoding='utf-8')
f.write(reversed_text)
f.close()

print("\nТекст в обратном порядке")
print(reversed_text)