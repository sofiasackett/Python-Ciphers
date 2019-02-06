# Sofia Sackett
# Caesar Cipher

# Import
import string

# Input
plaintext = input("Enter the text that you would like encrypted: ")
plaintext = plaintext.lower()
shift = int(input("Enter your desired shift: "))

# Function
def caesar (text, shift, alphabet=string.ascii_lowercase):
    alphaShift = alphabet[shift:] + alphabet[:shift]
    return text.translate(text.maketrans(alphabet, alphaShift))

# Output
print (caesar(plaintext, shift))





