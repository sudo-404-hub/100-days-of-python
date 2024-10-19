    # Writing short code
    # Define a function named convert that takes a list of numbers as its only parameter and returns a list of each number converted to a string.

    # For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].

    # What makes this tricky is that your function body must only contain a single line of code.



# try 1



# def convert(str):
#     if isinstance(str, list) == True:
#         my_list = []
#         for lists in str:
#             my_list.append(f"{lists}")
#         print(my_list)

#     else:
#         print("Enter the list only, i.e [1,2,3]")


# try 2

def convert(number):
    return list(map(str, number))

print(convert([1,2]))



# we can use map function to make it short.