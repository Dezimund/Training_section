print("input 5 numbers")
user_input = input()
numbers = int (user_input)

number1 = numbers % 10
number2 = numbers // 10 % 10
number3 = numbers // 100 % 10
number4 = numbers // 1000 % 10
number5 = numbers // 10000

print(number1,end="")
print(number2,end="")
print(number3,end="")
print(number4,end="")
print(number5)

