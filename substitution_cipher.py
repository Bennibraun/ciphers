import random
import os
import time

alphabet = ''

for i in range(32,127):
    alphabet += chr(i)

key = '`1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>? '

print(alphabet)
print(key)

def encrypt(message):
    loc = 0
    result = ''

    for letter in message:
        loc = alphabet.find(letter)
        result += key[loc]

    return result

def decrypt(message):
    loc = 0
    result = ''

    for letter in message:
        loc = key.find(letter)
        result += alphabet[loc]

    return result

def is_english(str):
    common_words = ['have','for','not','say','with','that','and','the']
    if any(word in str for word in common_words):
        return True
    return False

path = 'C:\\Users\\benja\\Desktop\\txt_files'

for filename in os.listdir(path):
    with open(os.path.join(path, filename),'r') as file:
        contents = file.read()
        if is_english(decrypt(contents)):
            print(filename + ' : ' + decrypt(contents))


print('done')
