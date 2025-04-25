# For loop --used to iterate through sequences and read each element of the sequences
# Syntax of For loop:
# for x in <sequences>:
# // for body statements


# print 1 to 10 numbers using for loop
for i in range(1,11):
    print(i,end=" ")


# print sum of first 10 numbers using for loop
sum1=0
for i in range(1,11):
    sum1+=i
print("\n",sum1)


# print elements in reverse order in list using for loop
li=[1,2,3,4,5]
for i in range(-1,-6,-1):
    print(li[i],end=" ")