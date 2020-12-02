# Version 2

print("Welcome to warrior calculator!\n")
print("1. Sum(+)")
print("2. Subtract(-)")
print("3. Multiply(*)")
print("4. Divide(/)")
opt = int(input("\nPlease one of the above options: "))
if opt <= 4:
    num1 = int(input("Please Enter First Number: "))
    num2 = int(input("Please Enter Second Number: "))
    if opt == 1:
        result = num1 + num2
        print("{0} + {1} = {2}".format(num1, num2, result))
    elif opt == 2:
        result = num1 - num2
        print("{0} - {1} = {2}".format(num1, num2, result))
    elif opt == 3:
        result = num1 * num2
        print("{0} * {1} = {2}".format(num1, num2, result))
    elif opt == 4:
        result = num1 / num2
        print("{0} / {1} = {2}".format(num1, num2, result))
else:
    print("Invalid Option!")
