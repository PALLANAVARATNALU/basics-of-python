# If-Elif-Else Statements Syntax
# if boolean expression:
#  // if body statements
# elif boolean expresssion:
# // elif body1 statements
# elif boolean expression:
# // elif body2 statements
# else:
# // else body statements


# Read temp from keyboard and check whether it is living temp or not
temp=int(input("enter the temperature:"))
if temp<0:
    print("it is too cold")
elif 0<temp<35:
    print("it is living temperature")
elif 35<temp<45:
    print("it is summer temperature")
else:
    print("it is hard to live")


# Read age from keyboard and print the age grouping as per the values
age=int(input("enter the age:"))
if 0<=age<=12:
    print("child")
elif 13<=age<19:
    print("teenager")
elif 20<=age<=59:
    print("adult")
else:
    print("senior citizens")