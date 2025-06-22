# Написати функцію say_hi, яка представить людину за переданими параметрами.
#
# Вхідні дані: Два аргументи рядок(str) та позитивне число(int)
#
# Функція має повернути рядок.
#
# Замініть pass на Ваше рішення.

def say_hi(name, age):
  print("Hi. My name is " + name + " and I'm " + str(age) + " years old.")
  return "Hi. My name is " + name + " and I'm " + str(age) + " years old."

assert say_hi("John", 30)
assert say_hi("Mary", 25)
