# Ваша функція is_even повинна повертати True якщо число парне, і False якщо число непарне.
#
# Вхідні дані: Ціле число.
#
# Вихідні дані: Логічний тип.

def is_even(digit):
    return digit % 2 == 0

print(is_even(2))
print(is_even(5))
print(is_even(0))
print(is_even(7))