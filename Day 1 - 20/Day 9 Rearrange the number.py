# 9. Rearrange the number
# To complete this challenge, write a function that accepts a number as a parameter. The function should return a number that’s the difference between the largest and smallest numbers that the digits can form in the number.

# For example, if the parameter is “213”, the function should return “198”, which is the result of 123 subtracted from 321.


num_list = []


def my_fun(number):
    for i in number:
        num_list.append(i)

    ascending_order   = sorted(num_list)
    descending_order = sorted(num_list, reverse=True)
    
    print(int(''.join(descending_order)) - int(''.join(ascending_order)))
    

my_fun(str(321))




