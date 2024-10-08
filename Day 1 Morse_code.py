# ## Day 1
# **1. Create a Morse code translator**
# We no longer use Morse code to transfer information, but that doesn’t mean you can’t 
# use it in a code challenge. Write a function in Python that takes in a string that can
#  have alphanumeric characters in lower or upper case.

# The string can also contain any special characters handled in Morse code, including 
# commas, colons, apostrophes, periods, exclamation marks, and question marks. The function 
# should return the Morse code equivalent for the string.

morse_code_dict = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "(": "-.--.", ")": "-.--.-", ",": "--..--",
    ".": ".-.-.-", "?": "..--..", "'": ".----.", ":": "---...", ";": "-.-.-.",
    "-": "-....-", "_": "..--.-", "/": "-..-.", "!": "-.-.--", "$": "...-..-",
    "&": ".-...", "+": ".-.-.", "=": "-...-", "@": ".--.-.", "¡": "--...-",
    "¿": "..-.-", "\"": ".-..-."
}

def encode(string):
    encoded_message = []
    for char in string:
        if char in morse_code_dict:
            encoded_message.append(morse_code_dict[char])
        else:
            encoded_message.append('')  # Append empty string for unsupported characters
    print(' '.join(encoded_message))

def decode(string):
    morse_to_char = {value: key for key, value in morse_code_dict.items()}
    decoded_message = []
    morse_words = string.split(' ')  # Split the input Morse code by spaces
    for morse_char in morse_words:
        if morse_char in morse_to_char:
            decoded_message.append(morse_to_char[morse_char])
        else:
            decoded_message.append('?')  # Append '?' for unsupported Morse code
    print(''.join(decoded_message))

while True:
    maininput = input("Enter 1 to encode \nEnter 2 to decode \nEnter q to exit :: ")
    if maininput == "1":
        encode(input("Enter your message to encode: ").upper())
    elif maininput == "2":
        decode(input("Enter your encrypted key to decode it: "))
    elif maininput == "q":
        print("BYE!!")
        break
    else:
        print("Invalid input. Please try again.")


    







