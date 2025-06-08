lst = [0, 1, 7, 2, 4, 8]
if len(lst) <= 0:
    print(0)
else:
    sum_lst = sum(lst[::2]) * lst[-1]
    print(sum_lst)

