# Sofia Sackett
# Atbash Cipher

import string

def main():
    question = print("Enter 'e' to encipher or 'd' to decipher.")
    mode = input("Choose mode: ")
    alpha = string.ascii_lowercase
    atbashAlpha = alpha[::-1]
    
    if mode == 'e' or mode == 'E':
        hiddenText  = input("Enter the text that you would like enciphered: ")
        print (encipher(hiddenText, alpha))
        
    elif mode == 'd' or mode == 'D':
        ciphertext = input("Enter the text that you would like deciphered: ")
        print (decipher(ciphertext, alpha))
        
    else:
        print("An error occured. Please enter 'e' to encipher or 'd' to decipher.")

def encipher (text, alphabet):
    return text.translate(text.maketrans(alphabet, atbashAlpha))

def decipher (text, alphabet):
    return text.translate(text.maketrans(atbashAlpha, alpha))

main()
