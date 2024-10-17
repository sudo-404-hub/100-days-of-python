# 7. Shadow sentences
# For the purpose of this challenge, shadow sentences are sentences where every word is the same length and order but without any of the same letters. Write a function that accepts two parameters that may or may not be shadows of each other. The function should return True if they are and False if they aren’t.
# An example would be “they are round” and “fold two times,” which are shadow sentences, while “his friends” and “our company” are not because both contain an r.

# so in easy word this task is like:
# To determine if two sentences are shadow sentences, you'll need to check two main criteria:
# Word Length: Each word in both sentences must be of the same length and in the same order.
# Unique Letters: No letter from any word in the first sentence should appear in the corresponding word of the second sentence.
# To implement this, compare the words one by one, ensuring both conditions are met. If they are, return True; otherwise, return False.



# # Try 1 :

# def my_fun(first_sentence, second_sentence):

#     l1 = list(first_sentence)
#     l2 = list(second_sentence)
#     len_l1 = len(l1)
#     len_l2 = len(l2)
#     if len_l1 == len_l2:
#         print("True")
#         print("Each word in both sentences are same length. ")
#     else:
#         print("False")
#         print("Each word in both sentences must be of the same length. ")


#     split_1 = first_sentence.split()
#     split_2 = second_sentence.split()
#     if len(split_1) == len(split_2):
#         print("True")

#         print("Each word in both sentences are in the same order")
#     else:
#         print("False")

#         print("Each word in both sentences must be of the same order")

# my_fun("The cat sat" , "A big dog")


# # Try 2:

# def my_fun(first_sentence, second_sentence):
#     i = 0

#     split_1 = first_sentence.split()
#     split_2 = second_sentence.split()

#     if len(split_1) == len(split_2):
#         i+=1
    
    
#     for w1, w2 in zip(split_1, split_2):
#         if set(w1) & set(w2):
#             i += 1
            
#     if i == 2:
#         print("True")
#     else:
#         print("False")

# my_fun("they are round", "fold two times")



# ## Try 3 
def shadow_sentences(sentence1, sentence2):
    words1 = sentence1.split()
    words2 = sentence2.split()
    
    if len(words1) != len(words2):
        return False
    
    for w1, w2 in zip(words1, words2):
        if len(w1) != len(w2) or set(w1) & set(w2):
            print(set(w1))
            return False
            
    return True



print(shadow_sentences("they are round", "fold two times")) # True shadow sentence
# print(shadow_sentences("his friends", "our company")) # False not shandow sentence


# Lerned:
# It uses a loop with zip() to iterate through pairs of corresponding words from both lists.

### 5. **Using `zip()` for Parallel Iteration**
# `zip()` allows you to iterate over multiple iterables in parallel.

# ```python
# names = ["Alice", "Bob", "Charlie"]
# scores = [85, 90, 95]

# for name, score in zip(names, scores):
#     print(f"{name}: {score}")
# ```


