# Напишіть функцію-генератор generate_cube_numbers, яка формує набір кубів чисел, починаючи з числа 2 до вказаної Вами величини. Тобто. генератор повинен працювати доти, поки генерується значення менше зазначеної величини.
#
# Нагадую, що вийти із генератора можна за допомогою return без параметрів.

def generate_cube_numbers(end):
    n = 2
    cube = n ** 3
    while cube <= end:
        yield cube
        n += 1
        cube = n ** 3

from inspect import isgenerator

gen = generate_cube_numbers(1)
print(isgenerator(gen))
print(list(generate_cube_numbers(10)))
print(list(generate_cube_numbers(100)))
print(list(generate_cube_numbers(1000)))