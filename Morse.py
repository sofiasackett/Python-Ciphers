# Sofia Sackett
# Morse Code 

def main():
    alphabet = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----'
}
    question = print("Enter 'e' to encipher or 'd' to decipher.")
    mode = input("Choose mode: ")

    if mode == 'e' or mode == 'E':
        text = input("Enter the text that you would like encrypted: ")
        text = text.upper()
        output = encipher(alphabet, text)
        print(output)

    elif mode == 'd' or mode == 'D':
        text = input("Enter the text that you would like deciphered with a '/' after every letter: ")
        if text[-1] != "/":
            text += "/"
        elif text[-1] == "/":
            pass
        output = decipher(alphabet, text)
        print(output.lower())

    else:
        print("An error occured. Please enter 'e' to encipher or 'd' to decipher.")

def encipher(alphabet, plaintext):
    ciphertext = ""
    for letter in plaintext:
        if letter != " ":
            ciphertext += alphabet[letter] + "/"
        elif letter == " ":
            ciphertext += " "
        else:
            print("An error occured. Please only enter letters and spaces.")
    return ciphertext

def decipher(alphabet, ciphertext):
    ciphertext += ' '
    plaintext = ''
    letters = ''
    for letter in ciphertext:
        if (letter != '/'):
            i = 0
            letters += letter
        else:
            i += 1
            if i == 2 :
                plaintext += ' '
            else:
                plaintext += list(alphabet.keys())[list(alphabet.values()).index(letters)]
                letters = ''
    return plaintext
main()

