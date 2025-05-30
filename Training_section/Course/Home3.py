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
