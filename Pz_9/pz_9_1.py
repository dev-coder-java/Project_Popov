# В озере водится несколько видов рыб. Три рыбака поймали рыб некоторых их имеющихся в озере видов.
# Определить, рыб каких видов поймал каждый рыбак и рыб каких видов, имеющихся в озере, не выловил ни один из рыбаков.
import random

ozero = {'карп', 'щука', 'лещ', 'карась','окунь'}
'''
z = random.choice(list(ozero))
a = random.choice(list(ozero))
c = random.choice(list(ozero))
b = random.choice(list(ozero))
print(a,z,c,b)
'''

fman1 = {'карп','щука'}
fman2 = {'щука','лещ'}
fman3 = {'лещ','карась'}
tot = fman1 | fman2 | fman3

print(ozero)
print(tot)
print("Рыбы которые не поймали: ", ozero-tot)


print(len(ozero))
print(len(tot))
print(fman1)
print(fman2)
print(fman3)
