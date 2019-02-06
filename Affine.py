# Sofia Sackett
#Affine Cipher

# Set up
import string
alphabet = list (map(chr, range(ord('a'), ord('z') + 1)))

# Directions
print("The Affine Cipher uses an encryption scheme based on three values, a and b")
print ("The variables a and b represent two numbers that must each be less than m and greater than 1.")
print("The first number, a, should have no factors in common with m.")

# Input
varA = int(input("Enter a value for variable a: "))
varB = int(input("Enter a value for variable b: "))
plaintext = input("Enter the text you would like encrypted: ")
plaintext = plaintext.replace(" ", "")
m = 26

# Function
def affine (a, b, plaintext):
    cipherText = ""
    
    for letter in plaintext:
        p = letter
        p = alphabet.index(letter)

        c = ((a*p) + b) % m
        cIndex = c % len(alphabet)
        cCharacter = alphabet[cIndex]
        
        cipherText += cCharacter

    return cipherText


# Output
print (affine(varA, varB, plaintext))
    
