# Anagrams
# Two strings are anagrams if you can make one from the other by rearranging the letters.

# Write a function named is_anagram that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.

# For example, the call is_anagram("typhoon", "opython") should return True while the call is_anagram("Alice", "Bob") should return False.



def is_anagram(word1, word2):
    split_word1 = word1.lower()
    split_word2 = word2.lower()

    return sorted(split_word1) == sorted(split_word2)
    

print(is_anagram("Alice", "Bob"))

print(is_anagram("typhoon", "opython"))


# An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once. For example, "cinema" is an anagram of "iceman." Anagrams are often used in puzzles, games, and wordplay, showcasing the flexibility of language.
