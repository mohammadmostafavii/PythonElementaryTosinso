############################ Function Example ####################################
# در این مثال از کابر خواسته می شود تا یک نام وارد کند
# و اینکار وقتی کاربر یک Enter خالی بزند متوقف می شود.
def enter_name():
    names = []
    while True:
        name = input("Please Enter You're Name: ")
        if name == '':
            break
        names.append(name)
    return names


enter_name()
