#Advanced datatype :
# 1.List
# 2.Tuple
# 3.Set
# 4.String
# 5.Range


#String read from keybaord
x=input("enter the name:") # denoted in single quotes and double quotes
print(x)


# string indexing
x="hello"
y="world"
print(x[1]) # +ve indexing
print(x[-2]) # -ve indexing


# Slicing Techniques on String
x="Python programming"
print(x[0:])  # print enter string
print(x[-6:]) # printing string by -ve indexing


#slicing technique2 using stepsize on String
x="python coding"
print(x[0::2]) # print the alternative indexed values here 2 is stepsize
print(x[0::-1]) # print the string in reverse order by +ve indexing
print(x[-1::-1]) # print the string in reverse order by -ve indexing


# mathematics with Strings
# it supports only 2 operations(+,*)
x="python"
y="language"
print(x+y)
print(x*5)
print(x*2+y)


# String format Techniques
x="python"
y='interpreter'
print(len(x)) #length of string x
print(len(y)) #length of string y
print("sum=",x+y)
print("sum of {} and {} is {}".format(x,y,x+y))
print(f"sum of{x} and {y} is {x+y}")


