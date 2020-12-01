# INTEGER
myInt1 = 10
myInt2 = -29


# FLOAT
myFl1 = 11.34
myFl2 = -.34


# STRING
myStr1 = "Hello World"
myStr2 = "Hello 'World'"
myStr3 = 'Hello "World"'


# LIST
myList = ["mohammad", 23, "ali", 7]
myList[1] = 24


# TUPLE
myTuple = ("mohammad", 23, "ali", 7)
# Tip: 'tuple' object doesn't support item assignment
# myTuple[1] = 24 This line not work because 'tuple' object doesn't updatable


# DICTIONARY
myDic = {'name': 'ali', 'age': 23, 'city': 'tehran'}
print(myDic['name'])
myDic['name'] = 'mohammad'


# MULTIPLE ASSIGNMENT
name1 = name2 = name3 = 'ali'
# name1 = 'ali'; name2 = 'ali'; name3 = 'ali'

name, age, city = 'ali', 7, 'tabriz'
# name = 'ali'; age = 7; city='tabriz'


# DELETE VARIABLE
name4 = 'ali'
del name4
