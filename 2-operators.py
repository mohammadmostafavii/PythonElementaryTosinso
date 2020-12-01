#################### SPECIAL ARITHMETIC OPERATORS ##########################
# % --> remain
# باقیمانده تقسیم عدد اول به عدد دوم را می دهد.
myRemain = 16 % 3  # myRemain = 1


# ** --> exponent
# عملگر توان که عدد اول را به توان عدد دوم می رساند.
myExponent = 4 ** 3  # myExponent = 64


# // --> floor division
# این عملگر نتیجه تقسیم را به سمت پایین گرد میکند و قسمت اعشاری را حذف میکند.
myFloor = 5 // 3  # myFloor = 1


#################### Assignment OPERATORS ##########################
num = 4
num += 2  # num = num + 2
num -= 3  # num = num - 3
num *= 5  # num = num * 5
num /= 2  # num = num / 2
num %= 2  # num = num % 2
num **= 4  # num = num ** 4
num //= 3  # num = num // 3


#################### LOGICAL OPERATORS ##########################
# and ~ &
myLogic1 = True and True  # myLogic1 = true
myLogic11 = True & True  # myLogic1 = true

# or ~ |
myLogic2 = True or False  # myLogic2 = true
myLogic22 = True | False  # myLogic2 = true

# not
myLogic3 = not True  # myLogic3 = false


#################### MEMBERSHIP OPERATORS ##########################
numbers = [1, 2, 3, 4, 5]
result1 = 4 in numbers  # result = true
result2 = 4 not in numbers  # result = false


#################### Tips ##########################
# ضرب یک رشته در یک عدد باعث می شود تا آن رشته به تعداد آن عدد چاپ شود.
tip1 = "ali" * 4  # "alialialiali"
