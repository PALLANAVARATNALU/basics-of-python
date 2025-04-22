# Conditional Statements:
# 1. If
# 2.If-Else
# 3.If-Elif-Else
# 4.Nested_If


#if statement syntax:
# if (Boolena Expressions):
#   //statements

# Read number from keyboard and print it is 2-digit number or not
num=int(input("enter the number:"))
if 10<=num<100:
    print(f"{num} id a 2-digit number")

# Read the char from keyboard and print it is a vowel or not
char_vowel=input("enter the character:")
if char_vowel in "aeiouAEIOU":
    print(f"{char_vowel} is a vowel character")

