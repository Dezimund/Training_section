l = [1]

if len(l) <= 0:
    print(l)
else:
    last_element = l.pop()
    l.insert(0, last_element)
    print(l)



