# Flatten a list
# Write a function that takes a list of lists and flattens it into a one-dimensional list.

# Name your function flatten. It should take a single parameter and return a list.

# For example, calling:

# flatten([[1, 2], [3, 4]])
# Should return the list:

# [1, 2, 3, 4]

# try 1:

my_list = []

def flatten(str):
    for i in str:
        my_list.extend(i) # Adds each element of an iterable to the end of the List # [1, 2, 3, 4]
    print(my_list)

flatten([[1, 2], [3, 4]])

# try 2: 

my_list = []

def flatten(str):
    for i in str:
        for j in i:
            my_list.append(j) # Used for adding elements to the end of the List. # [[1, 2], [3, 4]]
    print(my_list)

flatten([[1, 2], [3, 46]])







