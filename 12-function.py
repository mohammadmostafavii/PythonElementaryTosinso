############################ Function ####################################
########## Creating function ##########
# function defined using the def keyword
# Syntax:
# def function_name( parameters ):
#    function_body
#    return [expression]

########## Calling Functions ##########
# To call a function, use the function name followed by parenthesis:

def my_function():
    print("Hi From a Function!")


my_function()


########## Pass by reference vs value ##########
# All parameters in the Python language are passed by reference.
# It means if we change what a parameter refers to within a function,
# the change also reflects back in the calling function.
def chang_me1(param):
    param[0] = 20  # [20, 2, 3]


lst1 = [1, 2, 3]
chang_me1(lst1)
print(lst1)  # [20, 2, 3]


# Tip: When we pass a reference and change the received reference to something else,
# the connection between passed and received parameter is broken.
def chang_me2(param):
    param = [11, 12, 13]


lst2 = [1, 2, 3]
chang_me2(lst2)
print(lst2)  # [1, 2, 3]


def change_me3(param):
    param = 20


x = 10
change_me3(x)
print(x)  # 10


########## Arguments ##########
# Information can be passed into functions as arguments.
# Arguments are specified after the function name,inside the parentheses.
# We can add as many arguments as we want, just separate them with a comma.
# Tip: By default, parameters have a positional behavior and you need to inform them
# in the same order that they were defined.
# Type of Arguments:
#   1. Required arguments
#   2. Keyword arguments
#   3. Default arguments
#   4. Arbitrary(Variable-length) arguments, *args
#   5. Arbitrary Keyword Arguments, **kwargs

#   1. Required arguments
# Required arguments are the arguments passed to a function in correct positional order.
# Here, the number of arguments in the function call should match exactly with the function definition.
def print_mess1(fname, lname):
    print("Hi {0} {1}!".format(fname, lname))


print_mess1("mohammad", "ali")


#   2. keyword Arguments
# We can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.
def print_mess2(name, age):
    print("{0} is {1} years old!".format(name, age))


print_mess2(name="mohammad", age=23)
print_mess2(age=23, name="mohammad")


#   3. default Arguments
# A default argument is an argument that assumes a default value
# if a value is not provided in the function call for that argument.
def print_mess3(fname, lname="ali", age=23):
    print("Welcome {0} {1}! You're age is: {2}".format(fname, lname, age))


print_mess3("mohammad", "hasan", 13)
print_mess3("mohammad", age=69)
print_mess3("mohammad")


#   4. Arbitrary Arguments
# If we do not know how many arguments that will be passed into our function,
# add a * before the parameter name in the function definition.
def print_num1(*args):
    for i in args:
        print(i, end='\t')


print_num1(10, 11, 12, 13)  # 10 11	12 13
print()


#   5. Arbitrary Keyword Arguments
# If we do not know how many keyword arguments that will be passed into our function,
# add two asterisk: ** before the parameter name in the function definition.
def print_info(**kwargs):
    print("{0}: {1}".format(kwargs["name"], kwargs["age"]))


print_info(name="ali", age=7)  # ali: 7


########## Return ##########
# To let a function return a value, use the return statement:
def my_return(param):
    return param * 10


print(my_return(2))  # 20
print(my_return(3))  # 30


########## pass Statement ##########
# function definitions cannot be empty,
# but if we for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.
def my_pass():
    pass
