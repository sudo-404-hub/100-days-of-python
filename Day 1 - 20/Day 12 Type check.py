# Day 12 : Type check
# Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.

# For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.


def only_ints(char_1, char_2):
    
    if type(char_1) and type(char_2) == int:
        print("True")
    else:
        print("False")



only_ints(1,"a") # false

only_ints(1,2) # true

def capital_indexes(word):
    for index, word in enumerate(word):
        if word.isupper():
            print(index)

capital_indexes("heLLo")