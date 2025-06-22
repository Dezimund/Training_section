# На вхід функції correct_sentence передається речення. Необхідно повернути його виправлену копію так, щоб воно завжди починалося з великої літери та закінчувалося крапкою.
#
# Зверніть увагу, що не всі виправлення необхідні. Якщо речення вже закінчується крапкою, додавати ще одну не потрібно, це буде помилкою.
#
# Вхідні аргументи: string.
#
# Вихідні аргументи: string.
#
# Замість pass необхідно написати Ваше рішення.

def correct_sentence(text):
    if text[0].islower():
        text = text.capitalize()
    if not text[-1] == '.':
        text = text + '.'
    return text

print (correct_sentence("greetings, friends"))
print (correct_sentence("hello"))
print (correct_sentence("Greetings. Friends"))
print (correct_sentence("Greetings, friends."))
print (correct_sentence("greetings, friends."))

