# Напишіть функцію first_word, яка у переданому рядку знайде її перше слово.
#
# При розв'язанні задачі зверніть увагу на наступні моменти:
#
# У рядку можуть зустрічаються крапки та/або коми
# Рядок може починатися з літери або, наприклад, з пробілу або точки
# У слові може бути апостроф і він є частиною слова
# Весь текст може бути представлений лише одним словом та все
# Вхідні параметри: Рядок.
#
# Вихідні параметри: Рядок.

def first_word(text):
    text = text.replace(",", " ").replace(".", " ").replace(".."," ").replace("...", " ")
    text = text.strip()
    words = text.split()

    return words[0]



print(first_word("Hello world"))
print (first_word("greetings, friends"))
print (first_word("don't touch it"))
print (first_word(".., and so on ..."))
print (first_word("hi"))
print (first_word("Hello.World"))