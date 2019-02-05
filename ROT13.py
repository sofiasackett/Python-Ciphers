# Sofia Sackett
# ROT13 Cipher

# Import
import string

# Input
hiddenText = input("Enter the text that you would like encrypted: ")
hiddenText = hiddenText.lower()

# Function
def rot13 (text, alphabet=string.ascii_lowercase):
    rot13Alpha = alphabet[13:] + alphabet[:13]
    return text.translate(text.maketrans(alphabet, rot13Alpha))

# Output
print (rot13(hiddenText))
