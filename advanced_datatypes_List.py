list1=[10,20,30,40,50,60]  # homogenous list
print(list1)
print(type(list1))  # results datatype of input
print(len(list1))   # length of list
print(list1[3])     # fetching list elements by indexing
print(list1[::-1])  # print list elements in reverse order


list2=['python',12+4j,False,10,2.6]  # heterogenous list
print(type(list2))
print(list2[2])


# To add element in list
x=[10,20,30,40]
print(x)
new_li=x+[50]  # adding new element to existed list
print(new_li)

# list is muttable
x=[5,6,7,8,9,2]
print(x[0])  # 5 is output
print(x[1:4]) # 6,7,8 are the output
print(x[0]+x[-1]) # sum of the indexed elements as result

