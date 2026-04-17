#Из заданной строки отобразить только цифры. Использовать библиотеку string.
#Crpoka - TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand
#481 feet (147 metres) high.
import string

text = "Crpoka - TheGreatPyramidofKhufuatGizawasbuiltabout 2700 BC, 755 feet (230metres) longand 481 feet (147 metres) high."

result = "".join(filter(lambda char: char in string.digits, text))

print("Найденные цифры:", result)