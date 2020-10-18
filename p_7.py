
'''
7. Write a Python program to find the list in a list of lists whose sum
of elements is the highest.
'''
newlst = []
count = int(input("Enter the number of sublists : "))
for i in range(count):
    sublist = []
    count2 = int(input(F"Number of elements in the {i+1}th sublist : "))
    for j in range(count2):
        n = int(input(F"Enter {j+1}th element : "))
        sublist.append(n)
    newlst.append(sublist)

    hello = max(newlst, key=sum)

print("The sublist with highest sum is :")
print(hello)
