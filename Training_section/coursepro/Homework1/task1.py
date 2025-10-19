# 1.
# Напишіть функцію, яка приймає рядок і повертає його довжину.
# Створіть функцію, яка приймає два рядки і повертає об'єднаний рядок.

def length_string(user_input):
    return len(user_input)

def string_connection(first_user_input, second_user_input):
    return first_user_input + second_user_input

# 2.
# Реалізуйте функцію, яка приймає число і повертає його квадрат.
# Створіть функцію, яка приймає два числа і повертає їхню суму.
# Створіть функцію яка приймає 2 числа типу int, виконує операцію ділення та повертає чілу частину і залишок.

def power_of_two(user_input):
    return user_input ** 2

def summary(user_input_one,user_input_two):
    return user_input_one + user_input_two

def division(user_input_one,user_input_two):
    return float(user_input_one / user_input_two)

# 3.
# Напишіть функцію для обчислення середнього значення списку чисел.
# Реалізуйте функцію, яка приймає два списки і повертає список, який містить спільні елементи обох списків

def avg_list(user_input):
    return sum(user_input) / len(user_input)

def same_elements(user_input_one,user_input_two):
    return list(set(user_input_one) & set(user_input_two))

# 4.
# Створіть функцію, яка приймає словник і виводить всі ключі цього словника.
# Реалізуйте функцію, яка приймає два словники і повертає новий словник, який є об'єднанням обох словників.

def keys_dict(user_input):
    return user_input.keys()

def union_dicts(user_input_one,user_input_two):
    return {**user_input_one, **user_input_two}

# 5.
# Напишіть функцію, яка приймає дві множини і повертає їхнє об'єднання.
# Створіть функцію, яка перевіряє, чи є одна множина підмножиною іншої.

def intersection(user_input_one,user_input_two):
    return user_input_one.intersection(user_input_two)

def is_subset(user_input_one,user_input_two):
    return user_input_one.issubset(user_input_two)


# 6.
# Реалізуйте функцію, яка приймає число і виводить "Парне", якщо число парне, і "Непарне", якщо непарне.
# Створіть функцію, яка приймає список чисел і повертає новий список, що містить тільки парні числа.

def is_even(user_input):
    if user_input % 2 == 0:
        print("Even number")
    else:
        print("Odd number")


def even_list(user_input):
    result = []
    while user_input:
        if user_input[0] % 2 == 0:
            result.append(user_input[0])
        user_input.pop(0)
    return result

