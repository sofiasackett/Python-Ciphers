# Sofia Sackett
# Caesar Cipher

# Import
import string

# Input
plaintext = input("Enter the text that you would like encrypted: ")
plaintext = plaintext.lower()
plaintext = plaintext.replace(" ", "")
shift = int(input("Enter your desired shift: "))

# Function
def cipher (text, shift, alphabet=string.ascii_lowercase):
    alphaShift = alphabet[shift:] + alphabet[:shift]
    return text.translate(text.maketrans(alphabet, alphaShift))

# Output
print (cipher(plaintext, shift))




