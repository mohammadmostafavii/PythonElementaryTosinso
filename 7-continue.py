############################ continue ####################################
# The continue statement in Python returns the control to the beginning of the while loop.
# The continue statement rejects all the remaining statements
# in the current iteration of the loop and moves the control back to the top of the loop.
# The continue statement can be used in both while and for loops.
# در برنامه زیر اعداد زوج بین 1 تا 100 را با هم جمع می کنیم.

num = 1
result = 0
while num <= 100:
    if num % 2 != 0:
        num += 1
        continue
    else:
        result += num
        num += 1
print(result)
