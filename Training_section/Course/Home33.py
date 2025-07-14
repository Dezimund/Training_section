# Створити клас цифрового лічильника. У класі реалізувати методи:
#
# встановлення максимального значення лічильника,
# встановлення мінімального значення лічильника
# встановлення початкового значення лічильника
# метод step_up збільшує лічильник на 1. Метод можна викликати до тих пір, поки значення досягне максимуму. При досягненні максимуму слід викинути (raise) виняток ValueError, з описом, що досягнуто максимумуʼ
# метод step_down зменшує лічильник на 1. Метод можна викликати до тих пір, поки значення не досягне мінімуму. При досягненні мінімуму потрібно викинути (raise) виняток ValueError, з описом, що досягнутий мінімум
# повернення поточного значення лічильника
# Початкове, мінімальне та максимальне значення лічильника також можуть бути додані в метод ініціалізації екземпляра класу.
#
# Приблизний каркас для класу та варіанти перевірки. Вам потрібно дописати необхідне замість pass


class Counter:
    def __init__(self, current=1, min_value=0, max_value=10):
        self.min_value = min_value
        self.max_value = max_value
        if not (min_value <= current <= max_value):
            raise ValueError("Початкове значення має бути між мінімальним та максимальним значенням")
        self.current = current

    def set_current(self, start):
        if not (self.min_value <= start <= self.max_value):
            raise ValueError("Значення має бути між мінімальним та максимальним значенням")
        self.current = start

    def set_max(self, max_max):
        if max_max < self.min_value:
            raise ValueError("Максимальне значення не може бути меншим за мінімальне")
        if max_max < self.current:
            raise ValueError("Максимальне значення не може бути меншим за поточне")
        self.max_value = max_max

    def set_min(self, min_min):
        if min_min > self.max_value:
            raise ValueError("Мінімальне значення не може бути більшим за максимальне")
        if min_min > self.current:
            raise ValueError("Мінімальне значення не може бути більшим за поточне")
        self.min_value = min_min

    def step_up(self):
        if self.current >= self.max_value:
            raise ValueError("Досягнуто максимум")
        self.current += 1

    def step_down(self):
        if self.current <= self.min_value:
            raise ValueError("Досягнуто мінімум")
        self.current -= 1

    def get_current(self):
        return self.current


counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
print (counter.get_current())
try:
    counter.step_up()
except ValueError as e:
    print(e)
print (counter.get_current())

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
print (counter.get_current())
try:
    counter.step_down()
except ValueError as e:
    print(e)
print (counter.get_current())