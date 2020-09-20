# you don't need to add () to create tuples, unless it is inside a list and you want to create a tuple
t = 5, 11
x, y = t
print(t)
print(x, y)

# using collecting (*) to sign first value of list on head and the others on tail - 
# you can reverse it by changin to: *head, tail
head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)