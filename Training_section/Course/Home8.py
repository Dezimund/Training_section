# Створіть список випадкових чисел із випадковою кількістю елементів від 3 до 10.
#
# Ваше завдання - створити новий список з 3 елементів початкового списку - першим, третім і другим з кінця.

import random

length = random.randint(3, 10)
original_list = [random.randint(1, 100) for i in range(length)]
result = [original_list[0], original_list[2], original_list[-2]]

print("Original list: ", original_list)
print("Result list: ", result)
