user_input = int(input("Enter a number: "))
while user_input > 9:
    result = 1
    for digit in str(user_input):
        result *= int(digit)
    user_input = result

print(user_input)