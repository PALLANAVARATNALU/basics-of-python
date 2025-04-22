# Nested-if Statement : if inside anotherif statement present


# Read gender & age from keyboard and print the eligibility for marriage or not
age=int(input("enter the age:"))
gender=input("enter the gender:")
if gender=="male":
    if age>=21:
        print("eligible for marriage")
    else:
        print("not eligible for marriage")
elif gender=="female":
    if age>=18:
        print("eligible for marriage")
    else:
        print("not eligible for marriage")
else:
    print("not eligible")