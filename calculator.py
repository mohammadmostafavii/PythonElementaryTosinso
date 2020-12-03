# Final Version
def calculator(number1, number2, op):
    if op == '+':
        return number1 + number2
    elif op == '-':
        return number1 - number2
    elif op == '*':
        return number1 * number2
    elif op == '/':
        if number2 == 0:
            return 0
        else:
            return number1 / number2


print("Welcome To Warrior Calculator!!!")
while True:
    print('1. Sum(+)')
    print('2. Subtract(-)')
    print('3. Multiply(*)')
    print('4. Divide(/)')
    print('5. Exit')

    opt = input("Please Enter You're Operator: ")
    if opt == '5':
        break

    operators = '+-*/'
    if opt == '1' or opt == '2' or opt == '3' or opt == '4':
        opt = operators[int(opt) - 1]

    num1 = int(input("Please Enter You're First Number: "))
    num2 = int(input("Please Enter You're Second Number: "))

    result = calculator(num1, num2, opt)

    print("{0} {1} {2} = {3}".format(num1, opt, num2, result))
