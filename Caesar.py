# Sofia Sackett
# Caesar Cipher

import string

question = print("Enter 'e' to encipher or 'd' to decipher.")
mode = input("Choose mode: ")

# Encode
if mode == 'e' or mode == 'E':
    plaintext = input("Enter the text that you would like enciphered: ")
    plaintext = plaintext.lower()
    plaintext = plaintext.replace(" ", "")
    shift = int(input("Enter your desired shift: "))

    def encipher (text, shift, alphabet=string.ascii_lowercase):
        alphaShift = alphabet[shift:] + alphabet[:shift]
        return text.translate(text.maketrans(alphabet, alphaShift))

    print (encipher(plaintext, shift))

# Decode
elif mode == "d" or mode == 'D':
    ciphertext = input("Enter the text that you would like deciphered: ")
    ciphertext = ciphertext.lower()
    ciphertext = ciphertext.replace(" ", "")
    key = int(input("Enter the shift key: "))
        
    def decipher (ciphertext, key, alphabet=string.ascii_lowercase):
        keyShift = alphabet[key:] + alphabet[:key]
        return ciphertext.translate(ciphertext.maketrans(keyShift, alphabet))

    print(decipher(ciphertext, key))

else:
    print("An error occured. Please enter either 'e' to encipher or 'd' to decipher.")
        





