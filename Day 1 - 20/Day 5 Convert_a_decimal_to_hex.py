# 5. Convert a decimal to a hex
# For this challenge, you need to write a function in Python that accepts a string of ASCII characters. 
# It should return each character’s value as a hexadecimal string. 
# Separate each byte by a space, and return all alpha hexadecimal characters as lowercase.


def my_fun(inputt):


    for i in inputt:
        unicode_value = ord(i)
        hexx = hex(unicode_value)
        print(hexx[-2:] , end= " ")

        

my_fun("hello")

# learned :
# ord function help to convert a letter into a unicode value.
# unicode value  is a universal character encoding standard that assigns a unique code point to every character in virtually all writing systems, symbols, and emojis used worldwide.
# hex is a function that convert unicode into hex value. like 0x72 . 













