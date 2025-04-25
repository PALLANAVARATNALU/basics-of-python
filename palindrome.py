# Read the number from keyboard and check whether it is palindrome or not
# num1=int(input("enter the number:"))
# dummy_num=num1
# reverse_num=0
# while num1>0:
#     num2=num1%10
#     reverse_num=reverse_num*10+num2
#     num1=num1//10
# if dummy_num==reverse_num:
#     print(f"{dummy_num} is a palindrome")
# else:
#     print(f"{dummy_num} is not palindrome")


#  Read the input from keyboard and print string in reverse order
string1=input("enter the string:")
reverse_str=""
i=len(string1)-1
while i>=0:
    reverse_str+=string1[i]
    i-=1
if reverse_str==string1:
    print(f"{reverse_str} is a palindrome")
else:
    print(f"{reverse_str} is not a palindrome")
