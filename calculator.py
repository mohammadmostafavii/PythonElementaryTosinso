# Version 1
# This Version include "input", "output" and "Type Change"

num1 = input("Please Enter 1st Number: ")
num2 = input("Please Enter 2st Number: ")

# وقتی کاربر ما عدد را وارد می کند این عدد به صورت string ذخیره میشود و باید آن را به integer تبدیل کنیم،
# برای انجام این کار از تابع int استفاده می کنیم.

sum = int(num1) + int(num2)
division = int(num1) / int(num2)

print(num1, "+", num2, "=", sum)

# .2f --> یعنی تا دو رقم اعشار را نشان بده

print("{0} / {1} = {2:.2f}".format(num1, num2, division))
