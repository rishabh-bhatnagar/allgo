
'''
Write a Python program to count the number of strings where the
string length is 4 or more and the first and last character are same
from a given list of strings.
'''
print("Enter the elements of list with spacing : ")

new = [z for z in input().split()]

strings = 0

for i in new:

    if len(i) >= 4 and i[0] == i[-1]:

        strings = strings + 1

print("No. of the strings is : ", strings)
