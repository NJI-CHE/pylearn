#Conditional statemtns are used to give different outputs based
# different conditiond, this is decision making logically.
#Python supports the usual logical conditions from mathematics
# Equals: a == b 
# Not equal a != b
# Less than: a < b
#Less than or equal to a <= b
# Greater than; a > b
# Greater or equal to a >= b


a = 45
b = 50
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")



##Nested If statements
x = 11


if x > 10:
    print("Above ten, ")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20")
