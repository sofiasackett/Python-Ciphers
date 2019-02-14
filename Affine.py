# Sofia Sackett
#Affine Cipher

import string
lower = list (map(chr, range(ord('a'), ord('z') + 1)))
upper = list (map(chr, range(ord('A'), ord('Z') + 1)))
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+", ",", "-", ".", "/",
                  ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]
alphabet = lower + upper + symbols

def main():
    question = print("Enter 'e' to encipher or 'd' to decipher.")
    mode = input("Choose mode: ")
    m = int(len(alphabet))
    
    if (mode == 'e' or mode == 'E'):
        varA = int(input("Enter a value for variable a: "))
        varB = int(input("Enter a value for variable b: "))
        plaintext = input("Enter the text you would like enciphered: ")
        plaintext = plaintext.replace(" ", "")
        plaintext = plaintext.lower()
        print (encipher(varA, varB, m, plaintext))
        
    elif (mode == 'd' or mode == 'D'):
        varA = int(input("Enter the key for variable a: "))
        varB = int(input("Enter the key for variable b: "))
        ciphertext = input("Enter the text you would like deciphered: ")
        ciphertext = ciphertext.replace(" ", "")
        ciphertext = ciphertext.lower()
        print (decipher(varA, varB, m, ciphertext))

    else:
        print("An error occured. Please enter 'e' to encipher or 'd' to decipher.")

def encipher (a, b, m, plaintext):
    ciphertext = ""
    for letter in plaintext:
        p = letter
        p = alphabet.index(letter)
        c = ((a*p) + b) % m
        cIndex = c % m
        cCharacter = alphabet[cIndex]
        ciphertext += cCharacter
    return ciphertext
       
def find_mod_inverse(a, m):
    a = a % m
    for x in range (1, m):
        if ((a * x) % m == 1):
            return x
        
def decipher(a, b, m, ciphertext):
    plaintext = ""
    for letter in ciphertext:
        c = letter
        c = alphabet.index(letter)
        x = find_mod_inverse(a, m)
        p = x * (c-b) % m
        pIndex = p % m
        pCharacter = alphabet[pIndex]
        plaintext += pCharacter
    return plaintext

main()

    
