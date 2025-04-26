# Functions - Grouping set of instructions to perform a task
# Type of Functions :
# Pre-defined Functions
# User-defined Functions

# User-defined Functions -function defined by user for doing business logic
# Syntax:
# def function name:
# // function body
# function name() (function cslling)


# Example
def read():
    print("we are redaing")
    print("we are writing")
read()


# Function with parameters
# create a function with one parameter and print double that value
def double(x):
    print(x*2)
double(10)
double(20)


# create a function with two parameter and print sum of that values
def sum_of(x,y):
    print(x+y)
sum_of(10,20)


# Create a function of birthday wishes and use user input and print wishes
name=input("enter the name:")
def bdy_wishes(name):
    print(f"happy birthday to you {name}")
bdy_wishes(name)


# function with return
# return - used to send data outside of a function and exit from function
# Create a substract function with 2 parameter and print output outside of  afunction
def sub1(x,y):
    subs=x-y
    return subs
s1=sub1(205,103)
print(s1)
print(s1+50)