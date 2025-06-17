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

while True:
    print("Input first number:")
    first_number = float(input())
    print("Input second number:")
    second_number = float(input())
    print("Input sign:")
    sign = input()

    if sign == "+":
        print(first_number + second_number)
    elif sign == "-":
        print(first_number - second_number)
    elif sign == "*":
        print(first_number * second_number)
    elif sign == "/" and second_number != 0:
        print(first_number / second_number)
    else:
        print("Invalid operation!")

    print("\nWant to continue? (y/n):")
    continue_calc = input().lower()
    if continue_calc == 'y':
        continue
    elif continue_calc == 'n':
        break

print("Bye!")


