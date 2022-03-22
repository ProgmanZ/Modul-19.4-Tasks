# Задача 1. Пунктуация

punct = set()
punct = {'.', ',', ';', ':', '!', '?'}

user_string = input('Введите строку: ')
count = 0
for symbol in user_string:
    if symbol in punct:
        count += 1
print('Количество знаков пунктуации: ', count)