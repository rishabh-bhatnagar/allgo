'''
Write a Python program to check if a given key already exists
 in a dictionary.
'''
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

x = d.keys()
print("The dictionary has following keys :")
print(x)
print("                 ")

k = input("Enter the key to check : ")

if k in d:
    print(k, "is present in the dictionary")
else:
    print(k, "is not present int the dictionary")
