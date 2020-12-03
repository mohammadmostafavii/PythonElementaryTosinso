############################ RANGE ####################################
# The range() function returns a sequence of numbers,
# starting from 0 by default, and increments by 1 (by default),
# and stops before a specified number(stop - 1).
# Syntax --> range(start, stop, step)

# takes one argument --> range(stop)
for i in range(4):
    print(i)  # 0, 1, 2, 3

# takes two arguments --> range(start, stop)
for i in range(4, 8):
    print(i)  # 4, 5, 6, 7

# takes three arguments --> range(start, stop, step)
for i in range(12, 20, 3):
    print(i)  # 12, 15, 18

# Reverse
for i in range(20, 9, -2):
    print(i)

# Accessing range() with index value
index1 = range(10)[0]
print("first element: {0}".format(index1))

index2 = range(10)[-1]
print("last element: {0}".format(index2))

index3 = range(10)[3]  # 0 1 2 3 4 ... 9
print("forth element: {0}".format(index3))  # forth element: 3

lst = ["ali", "mohammad", "hassan", "hossein"]
for item in range(0, len(lst), 1):
    print(lst[item])
# Reverse
for item in range(len(lst) - 1, -1, -1):
    print(lst[item])
