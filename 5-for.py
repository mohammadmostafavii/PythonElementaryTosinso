################################ for statement ################################
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print("The Number is: {0}".format(n))
# The Number is: 1
# The Number is: 2
# The Number is: 3
# The Number is: 4
# The Number is: 5

message = "Hi ali!"
for n in message:
    print(n)
# H
# i
#
# a
# l
# i
# !

myTuple = (1, 2, 3, 4, 5)
total = 0
for n in myTuple:
    total += n
print("Sum is: {0}".format(total))  # Sum is: 15
