def sortWordsByLength(s):
    words = s.split()
    sorted_words = sorted(words, key=len)
    return ' '.join(sorted_words)
user = input("Введите предложение: ")
result = sortWordsByLength(user)
print(result)
