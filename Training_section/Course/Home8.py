import random

length = random.randint(3, 10)
original_list = [random.randint(1, 100) for i in range(length)]
result = [original_list[0], original_list[2], original_list[-2]]

print("Original list: ", original_list)
print("Result list: ", result)
