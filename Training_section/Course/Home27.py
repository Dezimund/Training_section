# Напишіть функцію-генератор prime_generator, яка повертатиме прості числа. Верхня межа цього діапазону визначається параметром цієї функції.
#
# Наприклад, виклик функції
#
# list(prime_generator(10)) повинен відповідати послідовності з чисел [2, 3, 5, 7] .
#
# Наступне число в цій послідовності - 11 і воно більше 10 тому воно не потрапляє в цей ряд

def prime_generator(end):
    n = 2
    while n <= end:
        if all(n % i != 0 for i in range(2, n)):
            yield n
        n += 1

from inspect import isgenerator

gen = prime_generator(1)
print(isgenerator(gen))
print(list(prime_generator(10)))
print(list(prime_generator(15)))
print(list(prime_generator(29)))