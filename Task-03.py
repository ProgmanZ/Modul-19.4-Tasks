# Задача 3. Различные цифры

def convert(list_or_set):
    result_func = ''
    for i in list_or_set:
        result_func += str(i)
    return result_func


user_string = set(input('Введите строку: '))

digit = {str(i) for i in list(range(0, 10))}
digit = digit & user_string
result = convert(digit)
result = sorted(result)
result = convert(result)

print('Различные цифры строки:', result)
