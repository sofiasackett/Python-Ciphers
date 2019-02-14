# Sofia Sackett
# Baconian Cipher

def main():
    alphabet = {'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa', 
            'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab', 
            'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba', 
            'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb', 
            'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 'Z':'bbaab'}
    question = print("Enter 'e' to encipher or 'd' to decipher.")
    mode = input("Choose mode: ")

    if mode == 'e' or mode == 'E':
        text = input("Enter the text that you would like encrypted: ")
        text = text.upper()
        output = encipher(alphabet, text)
        print(output.lower())

    elif mode == 'd' or mode == 'D':
        text = input("Enter the text that you would like deciphered: ")
        text = text.lower()
        output = decipher(alphabet, text)
        print(output.lower())

    else:
        print("An error occured. Please enter 'e' to encipher or 'd' to decipher.")

def encipher(alphabet, plaintext):
    ciphertext = ""
    for letter in plaintext:
        if letter != " ":
            ciphertext += alphabet[letter]
        elif letter == " ":
            ciphertext += " "
        else:
            print("An error occured. Please only enter letters and spaces.")
    return ciphertext

def decipher(alphabet, ciphertext):
    plaintext = ""
    i = 0
    while True:
        if i < len(ciphertext)-4:
            section = ciphertext [i:i + 5]
            if section[0] != " ":
                plaintext += list(alphabet.keys())[list(alphabet.values()).index(section)]
                i += 5
            else:
                plaintext += " "
                i += 1
        else:
            break
    return plaintext

main()
