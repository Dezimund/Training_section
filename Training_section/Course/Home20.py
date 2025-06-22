# Ваше завдання – написати функцію is_palindrome, яка перевірятиме, чи є рядок паліндромом.
#
# Паліндромом - це такий рядок, який читається однаково зліва направо і зправа наліво без урахування знаків пунктуації та розмірності букв.
#
# Функція приймає на вхід рядок, та повертає булеве значення True або False

def is_palindrome(text):
    text = ''.join(char.lower() for char in text if char.isalnum())
    return text == text[::-1]

print (is_palindrome('A man, a plan, a canal: Panama'))
print (is_palindrome('0P'))
print (is_palindrome('a.'))
print (is_palindrome('aurora'))