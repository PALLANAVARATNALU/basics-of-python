# print first 10  fibanocci series

num1=0
num2=1
next_num=0
while next_num<=10:
    print(num1,end=" ")
    num1,num2=num2,num1+num2
    next_num+=1


# print  sum of first 10  fibanocci series
num1 = 0
num2 = 1
next_num = 0
sum1=0
while next_num <= 10:
    sum1+=num1
    num1, num2 = num2, num1 + num2
    next_num += 1
print("\n",sum1)


# print all fibanocci numbers below 500
num1=0
num2=1
while num2<500:
    print(num1,end=" ")
    num1,num2=num2,num1+num2

# print all even fibanocci numbers below 1000 and in reverse order
num1=0
num2=1
while num2<1000:
    if num2%2==0:
        print("\n",num2,end=" ")
    num1,num2=num2,num1+num2


num1=0
num2=1
even_fib=[]
while num2<1000:
    if num2 %2 ==0:
        even_fib.append(num2)
    num1,num2=num2,num1+num2
index=len(even_fib)-1
while index>=0:
    print(even_fib[index])
    index-=1


# print all odd fibanocci numbers below 1000 and in reverse order
num1=0
num2=1
while num2<1000:
    if num2%2!=0:
        print(num2,end=" ")
    num1,num2=num2,num1+num2


num1=0
num2=1
even_fib=[]
while num2<1000:
    if num2 %2 !=0:
        even_fib.append(num2)
    num1,num2=num2,num1+num2
index=len(even_fib)-1
while index>=0:
    print(even_fib[index],end=" ")
    index-=1