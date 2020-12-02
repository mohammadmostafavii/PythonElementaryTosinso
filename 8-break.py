############################ break ####################################
# The break statement in Python terminates the current loop
# and resumes execution at the next statement
# The break statement can be used in both while and for loops.

num = 10
result = 0
while num >= 1:
    if num == 8:
        break
    result += num
    num -= 1
print(result)
