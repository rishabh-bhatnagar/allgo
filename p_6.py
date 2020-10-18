
'''
write a Python program to find common items from two lists.
'''
print("Enter elements(characters) of first list with spacing : ")

list1 = [x for x in input().split()]

print("Enter elements(characters) of second list with spacing : ")

list2 = [y for y in input().split()]

list1 = set(list1)    # converting lists into sets

if (set(list1).intersection(list2)):

     a = (set(list1).intersection(list2))

new = list(a)    # back from set to list
for i in new:
    print(i, end=" ")
