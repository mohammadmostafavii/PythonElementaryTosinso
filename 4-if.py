############################ if-else ####################################
num = int(input('Please enter a number: '))

if num % 2 == 0:
    print("{0} is even.".format(num))
else:
    print("{0} is Odd.".format(num))
############################ elif ####################################

name = input("Username: ")
password = int(input("Password: "))

if name == "ali" and password == 123:
    print("Hi {0}".format(name))
elif name == "mohammad" and password == 321:
    print("Hi {0}".format(name))
else:
    print("You're Password or Username is not valid!")
