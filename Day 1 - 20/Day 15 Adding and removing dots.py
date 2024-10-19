# Challenge 15
# Adding and removing dots
# Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".

# Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".

# If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

# (You may assume that the input to add_dots does not itself contain any dots.)


def add_dots(word):
    for i in range(len(word)):
        print(word[i], end="")
        if i < len(word) - 1:  # Check if it's not the last character
            print(".", end="")
    print()  # To add a newline at the end

add_dots("test")




def remove_dotes(word):
    for i in word:
        if i == ".":
            continue
        print(i, end="")

remove_dotes("t.e.s.t")


