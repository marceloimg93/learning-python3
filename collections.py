# list
l = ["Anne", "Rolf", "Kevin"]

# tuple -> it can not be modify - add or remove
t = ("Anne", "Rolf", "Kevin")

# set -> can not have duplicated elements and order is not garanteed
s = {"Anne", "Rolf", "Kevin"}

print(l[0])
print(t[0])

l[0] = "Robert"
print(l[0])

l.append("Smith")
print(l)
l.remove("Rolf")
print(l)

# set use ADD command because append adds at the end of list while SET does not have an order, you must use add method
s.add("John")
s.add("John") # SET does not allow duplicated values
print(s)