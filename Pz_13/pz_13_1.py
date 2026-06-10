#В исходном текстовом файле (hotline.txt) после фразы «Горячая линия» добавить фразу
# «Министерства образования Ростовской области», посчитать количество произведённых добавлений.
# Сколько номеров телефонов заканчивается на «03», «50».
# Вывести номера телефонов горячих линий, связанных с ЕГЭ/ГИА.

import re
filename = "hotline.txt"
try:
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print(f"Ошибка: файл '{filename}' не найден!")
    exit()

original_text = text
phrase = "Горячая линия"
add_phrase = " Министерства образования Ростовской области"

count_additions = text.count(phrase)
text = text.replace(phrase, phrase + add_phrase)
with open(filename, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Добавлено фраз «Министерства образования Ростовской области» — {count_additions} раз(а)")

phone_pattern = r'[\+]?[78]?\s?\(?\d{3}\)?\s?\d{3}[-]?\d{2}[-]?\d{2}'
phones = re.findall(phone_pattern, text)

ends_03 = [p for p in phones if p.strip()[-2:] == "03"]
ends_50 = [p for p in phones if p.strip()[-2:] == "50"]

print(f"\nНомеров, заканчивающихся на «03»: {len(ends_03)}")
print(f"Номеров, заканчивающихся на «50»: {len(ends_50)}")
print("\nНомера телефонов горячих линий по ЕГЭ/ГИА:")
ege_keywords = ["ЕГЭ", "ГИА", "ЕГЭ/ГИА"]
ege_phones = []

for line in text.splitlines():
    if any(kw in line for kw in ege_keywords):
        found_phones = re.findall(phone_pattern, line)
        for p in found_phones:
            if p not in ege_phones:
                ege_phones.append(p)
                print(f"{p}")

if not ege_phones:
    print("(Не найдено номеров по ЕГЭ/ГИА)")