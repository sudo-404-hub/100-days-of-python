# Middle letter
# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

# For example, mid("abc") should return "b" and mid("aaaa") should return "".


def mid(word):
    split_word = list(word)
    len_word = len(split_word)
    if len_word % 2 != 0:
        len_word -= 1
        print(word[len_word // 2])
    else:
        print(" ")

mid("middle")
