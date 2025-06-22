# Функція second_index приймає як параметри 2 рядки. Вам необхідно знайти індекс другого входження шуканого рядка у рядку для пошуку.
#
# Розберемо перший приклад, де необхідно знайти друге входження "s" в слові "sims". Якби нам треба було знайти її перше входження, то тут все просто: за допомогою функції index або find ми можемо дізнатися, що "s" - це перший символ у слові "sims", а значить індекс першого входження дорівнює 0. Але нам Необхідно визначити другу "s", а вона четверта за рахунком. Значить індекс другого входження (і у відповідь питання) дорівнює 3.
#
# Рядок, який потрібно знайти, може складатися з кількох символів.
#
# Input: Два рядки (String).
#
# Output: Int or None

def second_index(text, some_str):
    first = text.find(some_str)
    if first == -1:
        return None
    second = text.find(some_str, first + 1)
    if second == -1:
        return None
    return text.find(some_str, text.find(some_str) + 1)

print (second_index("sims", "s"))
print (second_index("hello world", "l"))
print (second_index("find the river", "e"))
print (second_index("hi", "h"))
print (second_index("Hello, hello", "lo"))