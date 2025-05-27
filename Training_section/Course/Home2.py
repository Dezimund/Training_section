print("input 5 numbers")
user_input = input()
numbers = int (user_input)

number1 = numbers % 10
number2 = numbers // 10 % 10
number3 = numbers // 100 % 10
number4 = numbers // 1000 % 10
number5 = numbers // 10000

print(f"{number1}{number2}{number3}{number4}{number5}")
