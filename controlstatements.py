# Control Statements:
# Break : used to stop the iteration
# Continue : used to skip the current iteration
# Pass: used to print nothing


# examples for using control Statements(break,continue,pass)
# break
for i in range(0,11):
    if i==5:
        break
    print(i,end=" ")


#Continue
for i in range(11):
    if i==5:
        continue
    print(i,end=" ")


# pass
for i in range(11):
    if i==5:
        pass
    print(i,end=" ")
