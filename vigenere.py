with open('C:\\Users\\bbraun0361\\Desktop\\txt_files\\file_012499.txt','r') as file:
    message = file.read()


key = 'enigma'

def shift(letter, key):
    while letter + key < 32:
        letter += 95
    while letter + key > 126:
        letter -= 95
    return chr(letter + key)

def encrypt(message, key):
    encrypted_message = ''
    for i in range(0, len(message)):
        encrypted_message += shift(ord(message[i]), ord(key[i%6]))
    return encrypted_message

def decrypt(message, key):
    decrypted_message = ''
    for i in range(0, len(message)):
        decrypted_message += shift(ord(message[i]), -(ord(key[i%6])))
    return decrypted_message

print(decrypt(message, key))
