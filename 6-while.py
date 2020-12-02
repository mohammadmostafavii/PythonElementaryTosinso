############################ while ####################################
# برنامه زیر اعداد 1 تا 100 را با هم جمع میکند و در متغیر result قرار می دهد.
num = 1
result = 0
while num <= 100:
    result += num
    num += 1
print(result)  # result = 5050

# برنامه زیر دو عدد گرفته و آن دو عدد و اعداد بینشان را باهم جمع می کند.
num1 = int(input("Please Enter 1st Number: "))
num2 = int(input("Please Enter 2st Number: "))
little = 0
big = 0
result = 0
if num1 <= num2:
    little = num1
    big = num2
else:
    little = num2
    big = num1
while little <= big:
    result += little
    little += 1
print(result)
