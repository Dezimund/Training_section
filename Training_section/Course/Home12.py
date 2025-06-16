import string

input_string = input("Enter a 2 letters (example: a-b): ")

start, end = input_string.split('-')
letters = string.ascii_letters
start_index = letters.index(start)
end_index = letters.index(end)

if end_index < start_index:
    start_index, end_index = end_index, start_index

result = letters[start_index:end_index + 1]
print(result)
