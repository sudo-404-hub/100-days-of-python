# # Day 4
# **4. Parse an encoded string**
# In this Python challenge, you need to write a function that accepts an encoded string as a parameter. 
# This string will contain a first name, last name, and an id.

# Values in the string can be separated by any number of zeros. The id is a numeric value but will contain
#  no zeros. The function should parse the string and return a Python dictionary that contains the first 
# , last name, and id values.

# An example input would be “Robert000Smith000123”. The function should return the following using that 
# input:

# { “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }



# def my_fun(encode_msg):
    
#     split_msg = encode_msg.split('000')
#     print("First name is : ",split_msg[0])
#     print("Last name is : ",split_msg[1])
#     print("ID is : ", split_msg[2])


# my_fun("Robert000Smith000123")


# mistake i was doing ---
# using for loop to split the string.

## improvement
# handel more or less then 3 zero.



# improvement done: now you can add multiple 0 between words.

def my_fun(encode_msg):
    
    split_msg = encode_msg.split('0')

    print("First name is : ",split_msg[0])

    for i in split_msg[1:-1]:
        if len(i) > 1:
            print("Last name is : ",i)

    print("ID is : ", split_msg[-1])


my_fun("Robert00000Smith00000000123")










