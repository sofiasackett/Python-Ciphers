# Sofia Sackett
# Keyword Cipher

def main():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    question = print("Enter 'e' to encipher or 'd' to decipher.")
    mode = input("Choose mode: ")
    
    if mode == 'e' or mode == 'E':
        plaintext = input("Enter the text that you would like enciphered: ").lower()
        keyword = input("Enter your keyword: ").lower()
        print(encipher(plaintext, alphabet, keyword))

    elif mode == 'd' or mode == 'D':
        ciphertext = input("Enter the text that you would like deciphered: ").lower()
        keyword = input("Enter your keyword: ").lower()
        keyword = ''.join(sorted(set(keyword), key=keyword.index))
        print(decipher(ciphertext, alphabet, keyword))
        
def encipher(text, alphabet, keyword):
    key = ""
    substr = ""
    for char in text:
        if char in alphabet:
            substr += char
    for char in keyword:
            if char not in key:
                key += char
    for char in alphabet:
        if char not in key:
            key += char      
    index = [alphabet.index(char) for char in substr]
    return "".join(key[indexKey] for indexKey in index)

def decipher(text, alphabet, keyword):
    cipherAlpha = keyword + ""
    for char in alphabet:
        if char not in keyword:
            cipherAlpha += char
    index = [cipherAlpha.index(char) for char in text]
    return "".join(alphabet[indexKey] for indexKey in index)
        
main()
