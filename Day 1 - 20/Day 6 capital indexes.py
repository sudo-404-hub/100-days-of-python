# Capital indexes
# Write a function named capital_indexes. The function takes a single parameter, which is a string.
#  Your function should return a list of all the indexes in the string that have capital letters.

# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].


# 1. method :

def capital_indexes(string):
    l1 = []
    for i in range(len(string)):
      if string[i].isupper():
        l1.append(i)
    print(l1)

capital_indexes("HeLlO")



# 2nd method : 
def capital_indexes(string):

  for index, string in enumerate(string):
      if string.isupper():
        print(index, end=" : ")  


capital_indexes("HeLlO")



# learning section : 

# ## enumerate
# enumerate is a built-in function that adds a counter to an iterable (like a list or a tuple) and returns it as an enumerated object. This can be particularly useful when you need both the index and the value of items in a loop.
# - **Purpose**: Adds a counter to an iterable, allowing access to both index and value in a loop.
  
  
# - **Syntax**: 
#   ```python
#   enumerate(iterable, start=0)
#   ```
#   - `iterable`: The collection (e.g., list, tuple).
#   - `start`: Optional; the starting index (default is 0).


# ```python
# fruits = ['apple', 'banana', 'cherry']

  
# hii = list(enumerate(fruits, start=0))

# print(hii)
# ```

# - **Basic Example**:
#   ```python
#   fruits = ['apple', 'banana', 'cherry']
#   for index, fruit in enumerate(fruits):
#       print(index, fruit)
#   ```
#   **Output**:
#   ```
#   0 apple
#   1 banana
#   2 cherry
#   ```

# - **Custom Starting Index**:
#   ```python
#   for index, fruit in enumerate(fruits, start=1):
#       print(index, fruit)
#   ```
#   **Output**:
#   ```
#   1 apple
#   2 banana
#   3 cherry
#   ```

