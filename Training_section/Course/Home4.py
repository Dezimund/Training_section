l = [12, 3, 4, 10]

if len(l) <= 1:
    print(l)
else:
    last_element = l.pop()
    l.insert(0, last_element)

print(l)

