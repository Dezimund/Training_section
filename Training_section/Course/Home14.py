# Ваше завдання — написати програму, яка перемножує всі цифри, введені користувачем цілого числа, поки воно не стане менше або дорівнювати 9.
#
# Користувач вводить число з клавіатури.

user_input = int(input("Enter a number: "))
while user_input > 9:
    result = 1
    for digit in str(user_input):
        result *= int(digit)
    user_input = result

print(user_input)