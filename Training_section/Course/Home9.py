# Користувач вводить рядок. Ваше завдання - перевірити, чи може цей рядок бути ім'ям змінної.
#
# Змінна не може:
#
# починатися з цифри
# містити великі літери,
# пробіл і знаки пунктуації (взяти можна тут string.punctuation), окрім нижнього підкреслення "_".
# бути жодним із зареєстрованих слів.
# При цьому повне ім'я змінної повино складатись не більш чим з одного нижнього підкреслення "_".
#
# Список зареєстрованих слів можна взяти із keyword.kwlist.
#
# У результаті перевірки на друк виводиться або True, якщо таке ім'я змінної допустимо, або False - якщо ні.
#
# Приклади імен змінних та результат перевірки (=> на друк виводити не потрібно :))

import string
import keyword

user_input = input("Enter a string: ")

if not user_input:
    print(False)
elif ' ' in user_input:
    print(False)
elif user_input[0].isdigit():
    print(False)
elif any(c.isupper() for c in user_input):
    print(False)
elif not all(c.isalnum() or c == '_' for c in user_input):
    print(False)
elif user_input in keyword.kwlist and len(user_input.split('_')) == 1:
    print(False)
elif user_input.count('_') > 1 and not any(c.isalpha() for c in user_input):
    print(False)
else:
    print(True)






