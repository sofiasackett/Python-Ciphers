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

        def encipher (text, alphabet):
            return text.translate(text.maketrans(alphabet, atbashAlpha))

        print (encipher(hiddenText, alpha))


    elif mode == 'd' or mode == 'D':
        ciphertext = input("Enter the text that you would like deciphered: ")

        def decipher (text, alphabet):
            return text.translate(text.maketrans(atbashAlpha, alpha))

        print (decipher(ciphertext, alpha))

    else:
        print("An error occured. Please enter 'e' to encipher or 'd' to decipher.")

main()
