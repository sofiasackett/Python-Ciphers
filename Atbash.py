# Sofia Sackett
# Atbash Cipher
# Reversed alphabet

# Import
import string

# Input
plaintext = input("Enter the text that you would like encrypted: ")

# Function
def atbash (text, alphabet = string.ascii_lowercase):
    atbashAlpha = alphabet[::-1]
    return text.translate(text.maketrans(alphabet, atbashAlpha))

# Output
print (atbash(plaintext))
