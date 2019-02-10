# Sofia Sackett
# ROT13 Cipher

import string

question = print("Enter 'e' to encipher or 'd' to decipher.")
mode = input("Choose mode: ")

alphabet = string.ascii_lowercase
rot13Alpha = alphabet[13:] + alphabet[:13]

if mode == 'e' or mode == 'E':
    plaintext = input("Enter the text that you would like encrypted: ")
    plaintext = plaintext.lower()
    plaintext = plaintext.replace(" ", "")

    def encipher (text, alphabet):
        return text.translate(text.maketrans(alphabet, rot13Alpha))

    print (encipher(plaintext, alphabet))

elif mode == "d" or mode == 'D':
    ciphertext = input("Enter the text that you would like deciphered: ")
    ciphertext = ciphertext.lower()
    ciphertext = ciphertext.replace(" ", "")

    def decipher (text, alphabet):
        return text.translate(text.maketrans(rot13Alpha, alphabet))

    print (decipher(ciphertext, alphabet))

else:
    print("An error occured. Please enter 'e' to encipher or 'd' to decipher.")
