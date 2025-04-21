# Arithmetic Operations of two numbers with int datatype
num1=int(input("enter the 1st number:")) # without int data type it consider as string
num2=int(input("enter the 2nd number:"))
num3 = num1 + num2   #addition
num4 = num1 - num2    #subtraction
num5 = num1 * num2    #multiplication
print(num3)  # sum of that two numbers
print(num4) 
print(num5)

# Addition Operation of three numbers without int datatype
no1= input("enter the num1 :")
no2= input("enter the num2 :")
no3 = input("enter the num3:")
print(no1 +no2+no3)     #it considers input as string by default it perform stringconcat


# Read Length and Breadth of rectangle from keyboard and print area & perimeter
len=float(input("enter the length :"))
brd=float(input("enter the breadth:"))
area=len * brd
perimeter=2(len+brd)
print(area)
print(perimeter)


# find the simple interest by read values from keyboard
p=int(input("enter the principal:"))
r=int(input("enter the rate:"))
t=int(input("enter the time :"))
si=(p*r*t)/100
print(si)

# find the area of circle  and read the radius from keyboard
r=int(input("enter the radius:"))
pi=3.14
area_circle=pi*(r^2)
print(area_circle)
