import string

text = input("Enter a sentence: ")
text = ''.join(i for i in text if i not in string.punctuation)
words = text.split()
result = '#' + ''.join(word.title() for word in words)

if len(result) > 140:
    print(result[:140] + "...")
else:
    print(result)