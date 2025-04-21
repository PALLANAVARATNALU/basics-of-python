# Tuple packing and unpacking
# Tuple Homogenous
t=(10,20,30,40)
print(type(t))
print(len(t))
t1=10,20,30,40
print(type(t1))

# Tuple Heterogenous
t2=("python",10,2.6,10+6j,True,20)
print(t2[-3:])

# Fetching elements from tuple using indexing
numb = (10, 20, 30, 40, 50, 60, 70, 80, 90)
print(numb[0::2])
print(numb[1::2])
print(numb[-1::-2])
print(numb[-2::-2])
print(numb[1:5])
