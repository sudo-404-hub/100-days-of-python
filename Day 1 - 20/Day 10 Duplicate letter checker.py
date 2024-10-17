# 10. Duplicate letter checker
# Create a function in Python that accepts one parameter: a string that’s a sentence. This function should return True if any word in that sentence contains duplicate letters and False if not.

# In your function, you want to check each word in the sentence for duplicate characters. So for every word, you'll check its individual characters to see if any character appears more than once.

# Try 1 : 

def has_duplicate_letters(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Check each word for duplicate letters
    for word in words:
        # Convert the word to a set to get unique letters
        unique_letters = set(word) #set  Build an unordered collection of unique elements
        
        
        # If the length of the set is less than the length of the word, it has duplicates
        if len(unique_letters) < len(word):
            return True
    
    return False

# Example :
print(has_duplicate_letters("hello world"))  # False
print(has_duplicate_letters("helo world"))  # true

print(has_duplicate_letters("I have a book."))            # True






# Try 2:

def has_duplicate_letters(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Check each word for duplicate letters
    for word in words:
        letter_count = {}

        for letter in word:
            # Count occurrences of each letter
            if letter in letter_count:
                # print(letter)
                return True  # Duplicate found
            letter_count[letter] = 1
    
    return False

# Example usage
print(has_duplicate_letters("this is god LEvel false"))  # False

print(has_duplicate_letters("I have a book."))            # True
print(has_duplicate_letters("Look at those ducks."))       # True



