# Sofia Sackett
# Latin Alphabet Cipher

def main():
    alphabet = list (map(chr, range(ord('a'), ord('z') + 2)))

    plaintext = input("Enter the text you would like enciphered: ")
    plaintext = plaintext.lower()
    print (encipher(alphabet, plaintext))

  
def encipher(alphabet, plaintext):
    ciphertext = ""
    for letter in plaintext:
        if letter != " ":
            p = alphabet.index(letter)
            p += 1
            ciphertext += str(p)
        elif letter == " ":
            ciphertext += " "
    return ciphertext
        
main()
