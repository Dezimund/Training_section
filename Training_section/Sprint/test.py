

var_one = 10
print(var_one)  # Виведе: 10
var_one = "Hello"
print(var_one)  # Виведе: Hello


# Отримання числового вводу від користувача
user_input = input("Enter a number: ")
coefficient = 2
# Перетворення введеного рядка на ціле число та множення на коефіцієнт
result = int(user_input) * coefficient
print(result)  # Виведе результат множення


# Отримання рядка від користувача
name = input("Enter your name: ")
print("Hello, " + name + "!")

# Отримання десяткового числа від користувача
decimal_input = input("Enter a decimal number: ")
decimal_number = float(decimal_input)
print(decimal_number)


person = {"name": "John", "age": 30}
person["city"] = "New York"  # Додавання пари ключ-значення
print(person)  # Виведе: {'name': 'John', 'age': 30, 'city': 'New York'}

person.update({"job": "Developer"})
print(person)  # Виведе: {'name': 'John', 'age': 30, 'city': 'New York', 'job': 'Developer'}
age = person.pop("age")
print(age)  # Виведе: 30
print(person)  # Виведе: {'name': 'John', 'city': 'New York', 'job': 'Developer'}