# Read the input from keyboard
number = input()
print(number)


# Type Conversion from one datatype to another------>int,float,complex,boolean

# int to other datatypes
x=10
y=float(x)   # int to float
z=complex(x)    # int to complex
k=bool(x)       # int to boolean
print(y)
print(z)
print(k)


#float to other datatypes
a=10.5
print(type(a)) # result <class float>
b=int(a) # float to int
c=complex(a) #float to complex
d=bool(a)   # float to boolean
print(b)
print(c)
print(d)


# complex to other datatypes
s=12+5j
# w=int(s)
# u=float(s)
v=bool(s)
# print(w)   # can't convert from complex to int
# print(u) # can't convert from complex to float
print(v)


# boolean to other datatypes
b=True
a1=int(b)
a2=float(b)
a3=complex(b)
print(a1)
print(a2)
print(a3)
