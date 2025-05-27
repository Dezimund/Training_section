print("Enter a string: ")
s = input()

snake_case = s.lower().replace(' ', '_')
print(snake_case)

CamelCase = snake_case.title().replace('_', '')
print(CamelCase)