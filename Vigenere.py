# Sofia Sackett
# Vigenere Cipher 
  
def main():
    question = print("Enter 'e' to encipher or 'd' to decipher.")
    mode = input("Choose mode: ")

    if mode == 'e' or mode == 'E':
        text = input("Enter the text that you would like encrypted: ").upper()
        keyword = input("Enter the keyword: ").upper()
        key = getKey(text, keyword) 
        print(encipher(text,key))

    elif mode == 'd' or mode == 'D':
        text = input("Enter the text that you would like deciphered: ").upper()
        keyword = input("Enter the keyword: ").upper()
        key = getKey(text, keyword)
        print(decipher(text, key))

# Copies key until it is the same length as the plaintext
def getKey(text, key): 
    key = list(key) 
    if len(text) == len(key): 
        return(key) 
    else: 
        for i in range(len(text) - len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 
      
def encipher(text, key): 
    ciphertext = [] 
    for i in range(len(text)): 
        x = (ord(text[i]) + ord(key[i])) % 26
        x += ord('A') 
        ciphertext.append(chr(x)) 
    return("" . join(ciphertext)) 
      
def decipher(ciphertext, key): 
    plaintext = [] 
    for i in range(len(ciphertext)): 
        x = (ord(ciphertext[i]) - ord(key[i]) + 26) % 26
        x += ord('A') 
        plaintext.append(chr(x)) 
    return("" . join(plaintext)) 
      
main()
