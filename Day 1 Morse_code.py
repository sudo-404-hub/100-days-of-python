# ## Day 1
# **1. Create a Morse code translator**
# We no longer use Morse code to transfer information, but that doesn’t mean you can’t 
# use it in a code challenge. Write a function in Python that takes in a string that can
#  have alphanumeric characters in lower or upper case.

# The string can also contain any special characters handled in Morse code, including 
# commas, colons, apostrophes, periods, exclamation marks, and question marks. The function 
# should return the Morse code equivalent for the string.


morse_code_dict = {"A": ".-","B": "-...","C": "-.-.","D": "-..","E": ".","F": "..-.","G": "--.","H": "....","I": "..","J": ".---","K": "-.-","L": ".-..","M": "--","N": "-.","O": "---","P": ".--.","Q": "--.-","R": ".-.","S": "...","T": "-","U": "..-","V": "...-","W": ".--","X": "-..-","Y": "-.--","Z": "--..","(": "-.--.",")": "-.--.-",",": "--..--",".": ".-.-.-","?": "..--..","'": ".----.",":": "---...",";": "-.-.-.","-": "-....-","_": "..--.-","/": "-..-.","!": "-.-.--","$": "...-..-","&": ".-...","+": ".-.-.","=": "-...-","@": ".--.-.","¡": "--...-","¿": "..-.-","\"": ".-..-."}

def encode(string):
    for me in string : # loop start
        print(morse_code_dict[me] , end=" ")


def decode(string):
    reversed_morse = {value: key for key, value in morse_code_dict.items()} # change the key to value and value to key of morse_code_dict
    newstring = string.split() # break the string where from where is space
    for me in newstring:
        print(reversed_morse[me], end="")

while True:
    maininput = input("Enter 1 to encode \n enter 2 to decode \n enter q to exit :: ")
    if maininput == "1":
        encode(input("Enter your message to encode : ").upper())
    if maininput == "2":
        decode(input("Enter you encryted key to decode it : "))
    if maininput == "q":
        print("BYE!!")




