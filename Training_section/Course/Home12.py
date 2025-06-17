# Користувач вводить через дефіс дві літери: Ваше завдання — написати програму, яка повертатиме всі символи між ними включно.
#
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
#
# Підказка: Використовуйте модуль string, у якому є string.ascii_letters, з усім набором потрібних букв

import string

input_string = input("Enter a 2 letters (example: a-b): ")

start, end = input_string.split('-')
letters = string.ascii_letters
start_index = letters.index(start)
end_index = letters.index(end)

if end_index < start_index:
    start_index, end_index = end_index, start_index

result = letters[start_index:end_index + 1]
print(result)
