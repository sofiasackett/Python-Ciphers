# Sofia Sackett
# XOR Cipher

def main():
    question = print("Enter 'e' to encipher or 'd' to decipher.")
    mode = input("Choose mode: ")

    if mode == 'e' or mode == 'E':
        text = input("Enter the text that you would like enciphered: ").lower()
        key = input("Enter the keyword: ").lower()
        print(encipher(text, key))
        
    elif mode == 'd' or mode == 'D':
        text = input("Enter the text that you would like deciphered: ")
        key = input("Enter the keyword: ").lower()
        print(decipher(text, key))
        
    else:
        print("An error occured. Please enter 'e' to encipher or 'd' to decipher.")
        
def encipher(text, key):
    ciphertext = ""
    count = 0
    for i in range(len(text)):
        container = ord(text[i]) ^ ord(key[count])
        ciphertext += hex(container)[2:].zfill(2)
        count += 1
        if count >= len(key):
            count = 0
    return ciphertext

def decipher(text, key):
    toUnicode = ""
    for i in range(0, len(text), 2):
        toUnicode += bytes.fromhex(text[i:i+2]).decode('utf-8')
    plaintext = ""
    count = 0
    for i in range(len(toUnicode)):
        container = ord(toUnicode[i]) ^ ord(key[count])
        plaintext += chr(container)
        count += 1
        if count >= len(key):
            count = 0
    return plaintext

main()
