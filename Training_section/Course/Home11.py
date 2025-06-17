# Користувач вводить рядок, Ваше завдання – перетворити рядок на hashtag.
#
# Декілька правил:
#
# ніяких символів з набору string.punctuation не повинно бути, у тому числі й пробілів;
# підсумкова довжина hashtag має бути не більше 140 символів.
# кожне слово починається з великої літери.
# якщо довжина фінішного хештегу більше 140 символів - обрізати підсумковий рядок до 140 символів.

import string

text = input("Enter a sentence: ")
text = ''.join(i for i in text if i not in string.punctuation)
words = text.split()
result = '#' + ''.join(word.title() for word in words)

if len(result) > 140:
    print(result[:140] + "...")
else:
    print(result)