# The format() method formats the specified value(s) and insert them inside the string's placeholder.
# The placeholder is defined using curly brackets: {}.
# syntax --> string.format(value1, value2...)

txt1 = "My name is {name}, I'm {age}".format(name='mohammad', age=23)
# txt1 = My name is mohammad, I'm 23

txt2 = "My name is {0}, I'm {1}".format("mohammad", 23)
# txt2 = My name is mohammad, I'm 23

txt3 = "My name is {}, I'm {}".format("mohammad", 23)
# txt3 = My name is mohammad, I'm 23

