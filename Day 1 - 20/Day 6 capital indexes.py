# Capital indexes
# Write a function named capital_indexes. The function takes a single parameter, which is a string.
#  Your function should return a list of all the indexes in the string that have capital letters.

# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].




def capital_indexes(string):
    l1 = []
    for i in range(len(string)):
      if string[i].isupper():
        l1.append(i)
    print(l1)

capital_indexes("HeLlO")




