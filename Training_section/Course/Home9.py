import string
import keyword

user_input = input("Enter a string: ")

if not user_input:
    print(False)
elif user_input[0].isdigit():
    print(False)
elif '__' in user_input:
    print(False)
elif any(i.isupper() for i in user_input):
    print(False)
elif any(i in string.punctuation.replace('_', '') for i in user_input):
    print(False)
elif user_input in keyword.kwlist:
    print(False)
else:
    print(True)


