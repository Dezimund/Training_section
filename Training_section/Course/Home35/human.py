class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Стать: {self.gender}, Вік: {self.age}, Ім'я: {self.first_name}, Прізвище: {self.last_name}"
