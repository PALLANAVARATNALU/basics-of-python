# If-Else Statement Syntax:
# if boolean expression:
#  //if body statements
# else:
#  // else body statements


# Read the age from keyboard and print the person is eligible to vote or not
age=int(input("enter the age:"))
if age>=18:
    print("person is eligible to vote")
else:
    print(" person is not eligible")


# Read the number from keyboard and check whether number is positive or negative
number=int(input("enter the number:"))
if number>=0:
    print(f"{number} is a positive number")
else:
    print(f"{number} is a negative number" )